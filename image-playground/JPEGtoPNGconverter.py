import os
import sys

from PIL import Image

# grab the first and second argument
jpeg_folder = sys.argv[1]
png_folder = sys.argv[2]

# check if new exist if not create it
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

# loop through pokedex and convert images to png
for filename in os.listdir(jpeg_folder):
    img = Image.open(f"{jpeg_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{png_folder}{clean_name}.png", "png")
    print("all done")
