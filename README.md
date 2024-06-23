
# Img2Length

Img2Length is a Python application that calculates the total length of images in a folder based on their widths. It supports various units of measurement, including miles, meters, yards, kilometers, centimeters, and millimeters.

## Features

-   Select a folder containing image files (JPG, PNG, GIF, BMP, TIFF, & WEBP)
-   Choose the desired unit of measurement (mile, meter, yard, km, cm, mm)
-   Option to include or exclude subfolders in the calculation
-   Display the total length of all images in the selected folder
-   Show folder statistics (total number of images, total file size, unique dimensions, smallest and highest resolutions)

## Requirements

-   Python 3.x
-   PySide6 (Qt for Python)
-   Pillow (Python Imaging Library)

## Installation
**Method 1:**
1. Download pre-compiled binary from [Releases](https://github.com/LyAhn/Img2Length/releases) (Windows only currently)
2. Run Img2Length.exe

**Method 2:**

3.  Clone the repository or download the source code.
4.  Install the required dependencies using pip:

```
pip install PySide6 Pillow

```

## Usage

1.  Run the  `img2length.py`  script.
2.  Click the "Browse" button to select the folder containing the images.
3.  Choose the desired unit of measurement from the dropdown menu.
4.  Check or uncheck the "Include subfolders?" checkbox to include or exclude subfolders in the calculation.
5.  The total length of all images in the selected folder will be displayed in the "Total Length:" label.
6.  Click the "Folder Info" menu item to view folder statistics in a separate dialog.

## Known Issues
Performance can suffer reading folders with large quantities of sub-folders
No icons
Progress bar not functioning

## Planned Features

1. Error logging
2. Optional Saving of Stats/Metadata
3. Additional file formats
4. Different modes including Length and Area
5. UI Rework/Improvement

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the  [GNU General Public License v3.0 License](https://github.com/LyAhn/Img2Length?tab=GPL-3.0-1-ov-file#GPL-3.0-1-ov-file).

## Acknowledgments

-   [PySide6](https://doc.qt.io/qtforpython/)  - Qt for Python
-   [Pillow](https://python-pillow.org/)  - Python Imaging Library