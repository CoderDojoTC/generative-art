import os
from PIL import Image

def resize_images(directory):
  for filename in os.listdir(directory):
    with Image.open(os.path.join(directory, filename)) as img:
      img = img.resize((512, 512))
      img.save(os.path.join(directory, filename))

