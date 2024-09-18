import os
from PIL import Image


def convert_to_webp(input_dir, output_dir, quality=80):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg")):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_dir, output_filename)

            # Check if the output file already exists
            if not os.path.exists(output_path):
                with Image.open(input_path) as img:
                    img.save(output_path, "WEBP", quality=quality)
                print(f"Converted: {filename} to {output_filename}")
            else:
                print(f"Skipped: {filename} (already converted)")


# Usage
input_directory = "imgs"
output_directory = "webp_imgs"
convert_to_webp(input_directory, output_directory)
