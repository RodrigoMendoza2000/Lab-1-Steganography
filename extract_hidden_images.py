# ----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 26-Aug-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

from PIL import Image
from PIL import UnidentifiedImageError
import sys
import re
import os


def process_image(file_name: str) -> None:
    """
    Extracts from the red, green, and blue channels
    the corresponding hidden 1-bit images placing the result
    in three 1-bit PNG images with the following suffixes after
    the original extensionless file-name
    
    Args:
        file_name (str): a file name of a PNG image.
    """
    file_split_text = os.path.splitext(file_name)
    if file_split_text[1] == ".png":
        try:
            image = Image.open(file_name)
            if image.mode == "RGB":
                # extract_hidden_images(image)

                pixin = image.load()  # type: ignore
                width, height = image.size

                output_image = Image.new('1', (width, height))
                pixout = output_image.load()  # type: ignore

                file_names_colors = ['red', 'green', 'blue']
                for i in range(3):  # for each color channel
                    for y in range(height):
                        for x in range(width):
                            r, g, b = pixin[x, y]
                            if i == 0:
                                if r & 1:
                                    pixout[x, y] = 1  # black

                                else:
                                    pixout[x, y] = 0  # white
                            elif i == 1:
                                if g & 1:
                                    pixout[x, y] = 1
                                else:
                                    pixout[x, y] = 0
                            elif i == 2:
                                if b & 1:
                                    pixout[x, y] = 1
                                else:
                                    pixout[x, y] = 0
                    output_image.save(f"{file_split_text[0]}"
                                    f"_channel_1_{file_names_colors[i]}.png")

            else:
                print("The mode of the file is not RGB.")
                sys.exit()
        except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError, AttributeError) as error:
            print(error)
    else:
        print("Error: The provided file name doesn't have a .png extension.")
        sys.exit()


if '__main__' == __name__:
    # Read the file name from the command line
    try:
        INPUT_FILE_NAME = sys.argv[1]
    except IndexError:
        print("Error: No file name provided.")
        sys.exit()

    process_image(INPUT_FILE_NAME)
