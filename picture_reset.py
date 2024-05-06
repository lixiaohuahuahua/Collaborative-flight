from PIL import Image
import os

# Example usage:
source_folder = 'E:/desktop/pic'
dest_folder = 'E:/desktop/reset'
new_width = 250
new_height = 250
prefix = 'search'


def resize_and_rename_images(source_folder, dest_folder, new_width, new_height, prefix):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # Create destination folder if it doesn't exist

    files = [f for f in os.listdir(source_folder) if
             f.endswith('.png') and os.path.isfile(os.path.join(source_folder, f))]
    for i, filename in enumerate(files):
        file_path = os.path.join(source_folder, filename)
        img = Image.open(file_path)
        img = img.resize((new_width, new_height), Image.LANCZOS)  # Resize image using LANCZOS filter for high quality

        new_filename = f"{prefix}_{i + 1}.png"  # Construct new filename
        new_file_path = os.path.join(dest_folder, new_filename)
        img.save(new_file_path, 'PNG')  # Save resized image with PNG format

        print(f"Resized and saved {new_filename} to {dest_folder}")


resize_and_rename_images(source_folder, dest_folder, new_width, new_height, prefix)
