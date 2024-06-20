import os
from os.path import dirname
from pathlib import Path

from PIL import Image


def try_load_image(directory):
    for filename in os.listdir(directory):
        print(".", end="")
        if filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            try:
                img = Image.open(image_path)
                img.resize((150, 150,), resample=True, reducing_gap=2)
            except (IOError, SyntaxError) as e:
                print('Bad file:', image_path)
                os.remove(image_path)


def rename_files_in_directory(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            base = os.path.splitext(filename)[0]
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, base + new_ext)
            )



# Replace with your directory path
directory_path = Path(dirname(__file__), '..', 'data', 'train').absolute()
try_load_image(directory_path)

# rename_files_in_directory(directory_path, '.jpg', '.png')
