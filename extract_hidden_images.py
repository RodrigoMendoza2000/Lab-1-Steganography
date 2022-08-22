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


# def extract_hidden_images(image: Image.Image) -> None:
#     pixin = image.load()  # type: ignore
#     width, height = image.size
    
#     output_image = Image.new('1', (width, height))
#     pixout = output_image.load()  # type: ignore
        
#     for element in range(1,4):
#         for y in range(height):
#             for x in range(width):
#                 MULTIPLE_COLOR_LIST[element]= pixin[x, y]
                
#                 if COLOR_LIST[element] & 1:
#                     pixout[x, y] = 1  # black
                    
#                 else:
#                     pixout[x, y] = 0  # white

#         output_image.save(OUT_LIST[element])

def process_image(file_name: str) -> None:
    if ".png" in file_name:
        image = Image.open(file_name)
        if image.mode == "RGB":
            # extract_hidden_images(image)
            
            
            pixin = image.load()  # type: ignore
            width, height = image.size
        
            output_image = Image.new('1', (width, height))
            pixout = output_image.load()  # type: ignore
            
            for y in range(height):
                for x in range(width):
                    r,_,_ = pixin[x, y]
                    if r & 1:
                        pixout[x, y] = 1  # black
                        
                    else:
                        pixout[x, y] = 0  # white
            output_image.save("scarlett_chanel_1_red.png")

      
            for y in range(height):
                for x in range(width):
                    _,g,_ = pixin[x, y]
                    if g & 1:
                        pixout[x, y] = 1  # black
                        
                    else:
                        pixout[x, y] = 0  # white

            output_image.save("scarlett_chanel_2_green.png")
            
            
            for y in range(height):
                for x in range(width):
                    _,_,b = pixin[x, y]
                    if b & 1:
                        pixout[x, y] = 1  # black
                        
                    else:
                        pixout[x, y] = 0  # white

            output_image.save("scarlett_chanel_3_blue.png")
            
        else:
            print("The mode of the file is not RGB.")
            sys.exit()
    else:
        print("Error: The provided file name doesn't have a .png extension.")
        sys.exit()
    
if '__main__' == __name__:
    INPUT_FILE_NAME = sys.argv[1] # Leer el nombre del archivo de entrada desde la terminal
    # INPUT_FILE_NAME = "scarlett.jpg"
    # INPUT_FILE_NAME = "scarlett.png" 
    
    process_image(INPUT_FILE_NAME)