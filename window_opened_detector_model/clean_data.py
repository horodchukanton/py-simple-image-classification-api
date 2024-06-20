import os
from os.path import dirname
from pathlib import Path

from PIL import Image


def try_load_image(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            try:
                img = Image.open(image_path)
                img.verify()
            except (IOError, SyntaxError) as e:
                print('Bad file:', image_path)
                os.remove(image_path)


# Replace with your directory path
directory_path = Path(dirname(__file__), '..', 'data', 'train').absolute()
try_load_image(directory_path)
