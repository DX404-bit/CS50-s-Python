import sys

# To treat those files as images and all the functionality that comes with the library
from PIL import Image

# Accumulate all of theses images one at a time from the command line
images = []

# Using a loop to iterate over all of them and just add them to this list 
# after open them with the library
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the first image but asking the library to append this other image to it as well
# not bracket zero but bracket one
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)