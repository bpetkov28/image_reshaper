# image_reshaper

## Overview

Image Reshaper is a command-line tool that processes images to meet specific company requirements. It performs the following tasks:

- Renames image files to ensure they don't contain spaces or dashes.
- Removes the image background and replaces it with a white background.
- Converts the image format to JPG.

## Prerequisites

Before using Image Reshaper, ensure you have the following:

- Python 3.x installed on your system.
- Necessary Python libraries: `Pillow` for image processing and 'rembg' for removing image background

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bpetkov28/image_reshaper.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd image_reshaper
   ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Image Reshaper program, follow these steps:

1. Open Command Prompt

2. Navigate to the image_reshaper Directory
   ```bash
   cd path\to\image_reshaper
   ```

3. Run the Program
   ```bash
   python reshape_images.py <input_folder> <output_folder>
   ```

Replace <input_folder> with the name of the folder containing the images you want to process, and <output_folder> with the name of the folder where the processed images will be saved.

## Example

If your input images are in a folder named to_reshape and you want to save the reshaped images in a folder named reshaped_images, you would run:

   python reshape_images.py to_reshape reshaped_images

## Notes

- Ensure that the input folder exists and contains images to be processed.
- The output folder will be created if it doesn't already exist.
- Images will be renamed to remove any spaces or dashes, have their background removed and replaced with white, and be saved in JPG format.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


Thank you for using the image_reshaper! Stay safe and compile images faster than ever.




