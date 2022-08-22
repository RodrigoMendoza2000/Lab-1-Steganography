#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 26-Aug-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A013 Rodrigo Alfredo Mendoza España
#----------------------------------------------------------

# CHECK LIST

# 1-. Takes as a command line argument the name of an RGB mode PNG file. 
#   he program should print an error message and quit under the following circumstances:
#
# - The name of the file was not provided as a command line argument. OKAY
# - The provided file name doesn’t have a .png extension. OKAY
# - An exception is raised when trying to open the image file. It’s important to specify 
#   the reason as part of the error message. OKAY
# - The mode of the file is not RGB. OKAY
#
# 2-. Extracts from the red, green, and blue channels the corresponding hidden 1-bit images placing the result in three 1-bit 
#   PNG images with the following suffixes after the original extensionless file-name :
#
# - file-name_channel_1_red.png
# - file-name_channel_2_green.png
# - file-name_channel_3_blue.png

import string
from PIL import Image
import sys

def process_image(file_name: str) -> None:
    if ".png" in file_name:
        with Image.open(file_name) as image:
            if image.mode == "RGB":
                image.show()
            else:
                print("The mode of the file is not RGB.")
                sys.exit()
    else:
        print("Error: The provided file name doesn't have a .png extension.")
        sys.exit()
    
    # with Image.open(INPUT_FILE_NAME) as input_file:
    #     pixin = input_file.load() # type: ignore
    #     width, height = input_file.size
        
    # output_image = Image.new('RGB', (width, height))
    # pixout = output_image.load() # type: ignore
    
    # for y in range(height):
    #     for x in range(width):
    #         r, g, b = pixin[x, y]
    #         pixout[x, y] = (r, 0, 0)
    
    # output_image.save(OUTPUT_FILE_NAME)
    
    


if '__main__' == __name__:
    # INPUT_FILE_NAME = sys.argv[1] # Leer el nombre del archivo de entrada desde la terminal
    # INPUT_FILE_NAME = "scarlett.jpg"
    INPUT_FILE_NAME = "scarlett.png"
    
    process_image(INPUT_FILE_NAME)