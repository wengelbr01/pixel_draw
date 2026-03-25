import os
import sys
from PIL import Image, ImageDraw

AQUAMARINE = (127, 255, 212)    # a
# A
BEIGE = (245, 245, 220)         # b
BLUE = (0, 0, 255)              # B
CLEAR = (0, 0, 0, 0)            # ' ', '\n'
# c
# C
# d
EMERALD = (80, 200, 120)        # e
# E
# f
# F
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
# h
# H
INDIGO = (75, 0, 130)
# I
# j
# J
# k
# K
LEMON = (255, 247, 0)           # l
LIME_GREEN = (50, 205, 50)      # L
MUD = (165, 42, 42)
# M
# n
# N
ORANGE = (255, 165, 0)
# O
PURPLE = (106, 13, 173)
# P
# q
# Q
RED = (255, 0, 0)
# R
# silver
# S
# taupe
# T
# u
# U
VIOLET = (143, 0, 255)
# V
WHITE = (255, 255, 255)
# W
BLACK = (0, 0, 0)               # x
# X
YELLOW = (255, 255, 0)
# Y
# zinc
# Z

text_filename = sys.argv[1]

# Open file and read into contents 
with open(text_filename, 'r') as f:
    contents = f.read()

# Split contents into strings by line
stringList = contents.split('\n')

# Set pixel size to 50
pixelSize = 50

# Set width and height of image to fit all pixels
width, height = len(max(stringList, key=len)) * pixelSize, len(stringList) * pixelSize

# Set image to rgba for alpha value to clear
image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

# Set variable draw to save typing ImageDraw.Draw(image) every time
draw = ImageDraw.Draw(image)

# for every string of text in the file
for index, string in enumerate(stringList):
    # for every character in the string
    for i, char in enumerate(string):
        # Set start x position to index of character in the string
        x0 = i * pixelSize
        # Set start y position to index of string in the file
        y0 = index * pixelSize
        # Set end x position to 50 plus start x position
        x1 = x0 + pixelSize
        # Set end y position to 50 plus start y position
        y1 = y0 + pixelSize
        if char == 'a':
            draw.rectangle((x0, y0, x1, y1), fill=AQUAMARINE)
        elif char == 'b':
            draw.rectangle((x0, y0, x1, y1), fill=BLUE)
        elif char == 'B':
            draw.rectangle((x0, y0, x1, y1), fill=BLACK)
        elif char == ' ':
            draw.rectangle((x0, y0, x1, y1), fill=CLEAR)
        elif char == '\n':
            draw.rectangle((x0, y0, x1, y1), fill=CLEAR)
        elif char == 'e':
            draw.rectangle((x0, y0, x1, y1), fill=EMERALD)
        elif char == 'g':
            draw.rectangle((x0, y0, x1, y1), fill=GREEN)
        elif char == 'G':
            draw.rectangle((x0, y0, x1, y1), fill=GRAY)
        elif char == 'i':
            draw.rectangle((x0, y0, x1, y1), fill=INDIGO)
        elif char == 'o':
            draw.rectangle((x0, y0, x1, y1), fill=ORANGE)
        elif char == 'p':
            draw.rectangle((x0, y0, x1, y1), fill=PURPLE)
        elif char == 'r':
            draw.rectangle((x0, y0, x1, y1), fill=RED)
        elif char == 'v':
            draw.rectangle((x0, y0, x1, y1), fill=VIOLET)
        elif char == 'w':
            draw.rectangle((x0, y0, x1, y1), fill=WHITE, outline=WHITE)
        elif char == 'x':
            draw.rectangle((x0, y0, x1, y1), fill=BLACK)
        elif char == 'y':
            draw.rectangle((x0, y0, x1, y1), fill=YELLOW)
        else:
            draw.rectangle((x0, y0, x1, y1), fill=CLEAR)



# Name the image file
base_name = sys.argv[2]
if not base_name:
    base_name = "untitled"

"""
TODO: Save file in a new folder
Ask if save location is okay
if not ask for a different save location
"""


filename = f"{base_name}.png"
counter = 1
while os.path.exists(filename):
    filename = f"{base_name}_{counter}.png"
    counter += 1

image.save(filename, 'PNG')

print(f"Image saved as {filename}")

# show image
show = input("Would you like to see the new image? (y/n)").strip()
if show == 'y':
    image.show()
