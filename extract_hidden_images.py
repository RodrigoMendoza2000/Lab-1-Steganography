#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 26-Aug-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A013 Rodrigo Alfredo Mendoza España
#----------------------------------------------------------

import string
from PIL import Image
import sys

def process_image(file_name: str) -> None:
    print(file_name) # Borrar para entregar
    
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
    INPUT_FILE_NAME = sys.argv[1] # Leer el nombre del archivo de entrada desde la terminal
    process_image(INPUT_FILE_NAME)