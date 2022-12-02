import os
from PIL import Image

def copy_and_resize_images(src_dir, dst_dir):
  if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
  for filename in os.listdir(src_dir):
    with Image.open(os.path.join(src_dir, filename)) as img:
      img = img.resize((512, 512))
      img.save(os.path.join(dst_dir, filename))

home = '/Users/dan/Documents/ws/generative-art/'
src_dir = home + 'data/img-src'
print(len(os.listdir(src_dir)))
dst_dir = home + 'data/resized'

copy_and_resize_images(src_dir, dst_dir)

