import os
import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:

        file1 = os.path.splitext(sys.argv[1])[1].lower() # os calls for root (everything before the last period) and extension (everything after last period)
        file2 = os.path.splitext(sys.argv[2])[1].lower() # [1] for the extension, [0] for the root
        if file1 not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        if file2 not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        if file1 != file2:
            sys.exit("Input and output have different extensions")

        else:
            shirtify(sys.argv[1], sys.argv[2])

def shirtify(before, after):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(before) as photo: # to open images, use Image.open instead of just open
            photo = ImageOps.fit(photo, size) # ImageOps contains functions already made to automatically "crop/ edit" images
            photo.paste(shirt, shirt)
            photo.save(after)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
