# Lab-1-Steganography

The practice of concealing messages or information within other nonsecret text or data.

There are three independent 1-bit images hidden in the least significant bit of every byte from each of the three color channels of the image.

Write a Python script called extract_hidden_images.py that:

1 -. Takes as a command line argument the name of an RGB mode PNG file. The program should print an error message and quit under the following circumstances:


i. The name of the file was not provided as a command line argument.

ii. The provided file name doesn’t have a .png extension.

iii. An exception is raised when trying to open the image file. It’s important to specify the reason as part of the error message.

iv. The mode of the file is not RGB.


2-. Extracts from the red, green, and blue channels the corresponding hidden 1-bit images placing the result in three 1-bit PNG images with the following suffixes after the original extensionless file-name :

- file-name_channel_1_red.png

- file-name_channel_2_green.png

- file-name_channel_3_blue.png
