from PIL import Image
from rembg import remove
import sys
import os
import re

# Get the directory paths from command line arguments
if len(sys.argv) != 3:
    print(f"Please enter exactly 3 command line arguments. You entered {len(sys.argv)}.")
    sys.exit(1)

else:
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

# Ensure the source directory exists
if not os.path.exists(input_dir):
    print(f"The directory {input_dir} does not exist")
    sys.exit(1)

# Create the target directory if it doesn't exist
if not os.path.exists(output_dir):
    try:
        os.makedirs(output_dir)
    except Exception as e:
        print(f"Failed to create directory {output_dir}: {e}")
        sys.exit(1)

#Renames the images in server required format
def rename_image(image_name):
    pattern = r'[ -]'
    replaced_image_name = re.sub(pattern, '_', image_name)
    return replaced_image_name

# Converts all images in required format
def convert_images(wokring_dir):
    image_extensions = ['.apng', '.avif', '.gif', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp', '.jpg']
    for image in os.listdir(wokring_dir):
        if any(image.endswith(extension) for extension in image_extensions):
            image_input_path = os.path.join(wokring_dir, image)
            image_name = os.path.splitext(image)[0]
            output_image_name = rename_image(image_name)
            image_output_path = os.path.join(output_dir, f"{output_image_name}.jpg")

            try:
                with Image.open(image_input_path) as img:
                    output_img = remove(img)
                    rgb_output_img = output_img.convert('RGB')
                    rgb_output_img.save(image_output_path, 'JPEG')
                    print(f"Converted {image} to {output_image_name}.jpg")
            except Exception as e:
                print(f"Failed to convert {image}: {e}")


if __name__ == '__main__':
    convert_images(input_dir)

