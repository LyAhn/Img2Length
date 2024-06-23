import sys
import os
from PIL import Image

# Increase the maximum image size that Pillow can handle
Image.MAX_IMAGE_PIXELS = None  # Remove the limit entirely

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QCheckBox, QPushButton
from form_ui import Ui_Img2Length
from ui_folderInfo import Ui_InfoDialog

class FolderInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfoDialog()
        self.ui.setupUi(self)

"""
Application configuration settings for the Img2Length tool.

This dictionary contains various metadata about the application, such as the version, name, author, and description.
"""
app_config = {
    "version": "0.0.1-alpha",
    "name": "Img2Length",
    "author": "LyAhn",
    "description": "Convert image files to a specified unit.",
}
# Sets the image extensions that will be counted globally
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

class Img2Length(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Img2Length()
        self.ui.setupUi(self)

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
            self.update_conversion()

    def convert_pixels(self, folder_path, unit, include_subfolders):
        total_length = 0
        conversion_factors = {
        "mile": 0.000000164578833,
        "meter": 0.0002645833,
        "yard": 0.0002893912,
        "km": 0.0000002645833,
        "cm": 0.02645833,
        "mm": 0.2645833
    }

        def process_image(image_path):
            with Image.open(image_path) as image:
                return image.size[0] * conversion_factors[unit]


        if include_subfolders:
            for root, _, files in os.walk(folder_path):
                for filename in files:
                    if filename.lower().endswith(image_extensions):
                        total_length += process_image(os.path.join(root, filename))
        else:
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(image_extensions):
                    total_length += process_image(os.path.join(folder_path, filename))

        return f"Total Length: {total_length:.2f} {unit}"


    def update_conversion(self):
        unit = self.ui.unitComboBox.currentText()
        include_subfolders = self.ui.SubfoldersCheckBox.isChecked()

        if not self.folder_path:
            self.ui.converted_label.setText(f"Selected unit: {unit}")
            return

        try:
            self.ui.progressBar.setValue(0)
            converted_length = self.convert_pixels(self.folder_path, unit, include_subfolders)
            self.ui.converted_label.setText(str(converted_length))
            self.update_folder_info(include_subfolders)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

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
            QMessageBox.critical(self, "Error", str(e))

    def extract_metadata(self, folder_path, include_subfolders):
        # Initialize variables to store metadata and statistics
        total_count = 0
        total_file_size = 0
        unique_dimensions = set()
        min_resolution = (float('inf'), float('inf'))
        max_resolution = (0, 0)

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
        else:
            # Iterate over all image files in the folder (excluding subfolders)
            for filename in os.listdir(folder_path):
                if filename.endswith(image_extensions):
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

        # Return the collected metadata and statistics
        return total_count, total_file_size, len(unique_dimensions), min_resolution, max_resolution


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Img2Length()
    window.show()
    sys.exit(app.exec())
