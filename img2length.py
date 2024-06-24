# Copyright (C) 2024 LyAhn <erm@jezz.wtf>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import sys
import os
import logging
from PIL import Image
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QCheckBox, QPushButton
from form_ui import Ui_Img2Length
from ui_folderInfo import Ui_InfoDialog


"""

Application configuration settings for the Img2Length tool.

This dictionary contains various metadata about the application, such as the version, name, author, and description.
"""
app_config = {
    "version": "0.0.2-alpha",
    "name": "Img2Length",
    "author": "LyAhn",
    "description": "Convert image files to a specified unit.",
}

# Set up logging
log_file = 'img2length.log'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"Application started - Version: {app_config['version']}")

# Increase the maximum image size that Pillow can handle
Image.MAX_IMAGE_PIXELS = None  # Remove the limit temporarily (not the best solution)

class FolderInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfoDialog()
        self.ui.setupUi(self)
        logging.info("FolderInfoDialog (Stats) initialized")



# Sets the image extensions that will be counted globally
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

class Img2Length(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Img2Length()
        self.ui.setupUi(self)
        logging.info("Img2Length initializing...")

        # Connect signals and slots
        self.ui.browseButton.clicked.connect(self.browse_folders)
        self.ui.unitComboBox.currentTextChanged.connect(self.update_conversion)
        self.ui.SubfoldersCheckBox.stateChanged.connect(self.update_conversion)

        # Remove the resize grip from main window
        self.statusBar().setSizeGripEnabled(False)

        # Adds version number to title bar
        self.setWindowTitle(f"{app_config['name']} - {app_config['version']}")

        # Create an instance of the FolderInfoDialog
        self.folder_info_dialog = FolderInfoDialog(self)
        # Connect the actionFolder_Info menu item to show the dialog
        self.ui.actionFolder_Info.triggered.connect(self.folder_info_dialog.show)

        self.folder_path = ""

        #self.folder_info_dialog = QDialog(self) -- Removing this fixed the phantom unpopulated dialog.
        self.folder_info_ui = Ui_InfoDialog()
        self.folder_info_ui.setupUi(self.folder_info_dialog)
        logging.info("Img2Length initialized")

    def count_files(self, folder_path, include_subfolders):
        total_files = sum(
            1 for root, _, files in os.walk(folder_path)
            if any(file.endswith((image_extensions)) for file in files)
        ) if include_subfolders else sum(
            1 for file in os.listdir(folder_path)
            if file.endswith((image_extensions))
        )
        return total_files

    def show_folder_info_dialog(self):
        self.folder_info_dialog.QDialog(self)
        self.folder_info_ui = Ui_InfoDialog()
        self.folder_info_ui.setupUi(self.folder_info_dialog)

    def browse_folders(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_path = folder_path
            self.ui.folder_label.setText(f"Selected Folder: {folder_path}")
            logging.info(f"Selected folder: {folder_path}")
            self.update_conversion()

    def convert_pixels(self, folder_path, unit, include_subfolders):
        total_length = 0
        conversion_factors = {
            "mile": 0.000000164578833,
            "metre": 0.0002645833,
            "yard": 0.0002893912,
            "km": 0.0000002645833,
            "cm": 0.02645833,
            "mm": 0.2645833
    }

        logging.info(f"Starting conversion: Folder={folder_path}, Unit={unit}, IncludeSubfolders={include_subfolders}")

        def process_image(image_path):
            try:
                with Image.open(image_path) as image:
                    return image.size[0] * conversion_factors[unit]
            except (IOError, OSError) as e:
                logging.error(f"Error processing image {image_path}: {str(e)}")
                QMessageBox.critical(self, "Error", f"Error processing image {image_path}: {str(e)}")
            return 0

        try:
            if include_subfolders:
                for root, _, files in os.walk(folder_path):
                    for filename in files:
                        if filename.lower().endswith(image_extensions):
                            total_length += process_image(os.path.join(root, filename))
            else:
                for filename in os.listdir(folder_path):
                    if filename.lower().endswith(image_extensions):
                        total_length += process_image(os.path.join(folder_path, filename))
        except Exception as e:
            logging.error(f"Error during conversion: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error during conversion: {str(e)}")

        logging.info(f"Conversion completed. Total Length: {total_length:.2f} {unit}")
        return f"Total Length: {total_length:.2f} {unit}"


    def update_conversion(self):
        unit = self.ui.unitComboBox.currentText()
        include_subfolders = self.ui.SubfoldersCheckBox.isChecked()
        
        logging.info(f"Updating conversion: Unit={unit}, IncludeSubfolders={include_subfolders}")


        if not self.folder_path:
            self.ui.converted_label.setText(f"Selected unit: {unit}")
            return

        try:
            self.ui.progressBar.setValue(0)
            converted_length = self.convert_pixels(self.folder_path, unit, include_subfolders)
            self.ui.converted_label.setText(str(converted_length))
            self.update_folder_info(include_subfolders)
        except Exception as e:
            error_message = f"Error during conversion: {str(e)}"
            logging.error(error_message)
            QMessageBox.critical(self, "Error", error_message)
        finally:
            self.ui.progressBar.setValue(100)

    def update_folder_info(self, include_subfolders):
        try:
            total_count, total_file_size, unique_dimensions_count, min_resolution, max_resolution = self.extract_metadata(self.folder_path, include_subfolders)
            self.folder_info_ui.ttlImgLabel.setText(str(total_count))
            self.folder_info_ui.ttFileSizeLabel.setText(f"{total_file_size / (1024 * 1024):.2f} MB")
            self.folder_info_ui.uniqueDimLabel.setText(str(unique_dimensions_count))
            self.folder_info_ui.smallResLabel.setText(f"{min_resolution[0]} x {min_resolution[1]}")
            self.folder_info_ui.highResLabel.setText(f"{max_resolution[0]} x {max_resolution[1]}")

            self.folder_info_dialog.show()
        except Exception as e:
            QMessageBox.critical(self, "Error updating folder info", str(e))
            logging.error("Error updating folder info: " + str(e))

    def extract_metadata(self, folder_path, include_subfolders):
        logging.info(f"Extracting metadata from folder: {folder_path}, Include Subfolders={include_subfolders}")

        # Initialize variables to store metadata and statistics
        total_count = 0
        total_file_size = 0
        unique_dimensions = set()
        min_resolution = (float('inf'), float('inf'))
        max_resolution = (0, 0)
        
        try:

            if include_subfolders:
                # Iterate over all files in the folder and its subfolders
                for root, dirs, files in os.walk(folder_path):
                    for filename in files:
                        if filename.endswith(image_extensions):
                            # Open the image and extract metadata
                            image_path = os.path.join(root, filename)
                            image = Image.open(image_path)
                            width, height = image.size
                            file_size = os.path.getsize(image_path)

                            # Update metadata and statistics
                            total_count += 1
                            total_file_size += file_size
                            unique_dimensions.add((width, height))
                            min_resolution = min(min_resolution, (width, height), key=lambda x: x[0] * x[1])
                            max_resolution = max(max_resolution, (width, height), key=lambda x: x[0] * x[1])
        except (IOError, OSError) as e:
                        logging.error(f"Error processing image {image_path}: {str(e)}")
                        QMessageBox.critical(self, "Error", f"Error processing image {image_path}: {str(e)}")
        else:
            # Iterate over all image files in the folder (excluding subfolders)
            for filename in os.listdir(folder_path):
                if filename.endswith(image_extensions):
                    try:
                        # Open the image and extract metadata
                        image_path = os.path.join(folder_path, filename)
                        image = Image.open(image_path)
                        width, height = image.size
                        file_size = os.path.getsize(image_path)

                        # Update metadata and statistics
                        total_count += 1
                        total_file_size += file_size
                        unique_dimensions.add((width, height))
                        min_resolution = min(min_resolution, (width, height), key=lambda x: x[0] * x[1])
                        max_resolution = max(max_resolution, (width, height), key=lambda x: x[0] * x[1])
                    except (IOError, OSError) as e:
                        logging.error(f"Error processing image {image_path}: {str(e)}")
                        QMessageBox.critical(self, "Error", f"Error processing image {image_path}: {str(e)}")

        logging.info(f"Metadata extraction completed. Total count: {total_count}, Total file size: {total_file_size}, Unique dimensions: {len(unique_dimensions)}, Min resolution: {min_resolution}, Max resolution: {max_resolution}")
        # Return the collected metadata and statistics
        return total_count, total_file_size, len(unique_dimensions), min_resolution, max_resolution


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = Img2Length()
        window.show()
        sys.exit(app.exec())
    except:
        logging.critical(f"Critical error: {str(e)}")
        QMessageBox.critical(None, "Critical Error", f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
