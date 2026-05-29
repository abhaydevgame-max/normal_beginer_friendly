# ==============================
# PYTHON BEGINNER EXAMPLE FILE
# ==============================

# Importing the random module
# This module helps generate random numbers and choices
import random

# Importing everything from random module
# Not recommended in large projects, but okay for learning
from random import *

# Importing pygame and renaming it as "pg"
# pg is shorter and easier to type
import pygame as pg


# ==============================
# BASIC VARIABLES
# ==============================

name = "Python"      # String (text)
num1 = 123           # Integer (whole number)
num2 = 12.2          # Float (decimal number)

# List -> mutable (can change values)
list1 = ["list", 123, "in", "python"]

# Printing a value from list using index
# Index starts from 0
print(list1[1])

# Tuple -> immutable (cannot change values)
tup1 = (12, 21.29, 30)

# Dictionary -> key : value pairs
dict1 = {
    "harry": 132,
    12: "lost",
    True: None
}

print(dict1)


# ==============================
# MULTI LINE STRING
# ==============================

'''
This is a multi-line string.
People sometimes use it like comments.
'''


# ==============================
# FUNCTIONS
# ==============================

# Function for greeting user
def func(name):
    print(name, "hello how are you?")


# Taking input from user
user = input("Enter your name: ")

# Calling the function
func(user)


# ==============================
# BASIC CALCULATOR
# ==============================

# Input always comes as string
# So converting to integer using int()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# sum() needs iterable like list
print("Using sum function:", sum([a, b]))


# ==============================
# PYGAME SECTION
# ==============================

# Initializing pygame
pg.init()


class Game:

    # Constructor method
    # Runs automatically when object is created
    def __init__(self, height, width):

        # Saving width and height
        self.width = width
        self.height = height

        # Resolution tuple
        self.RES = (self.width, self.height)

        # Creating game window
        self.screen = pg.display.set_mode(self.RES)

        # Window title
        pg.display.set_caption("Beginner Pygame Window")

        # Clock used for FPS control
        self.clock = pg.time.Clock()

    # Main game loop
    def run_game(self):

        while True:

            # Checking events
            for event in pg.event.get():

                # If user presses close button
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            # Filling screen with black color
            self.screen.fill((0, 0, 0))

            # Updating display
            pg.display.update()

            # Limiting FPS to 60
            self.clock.tick(60)


# ==============================
# STARTING THE GAME
# ==============================

# Creating object from Game class
game = Game(600, 800)

# Running the game
game.run_game()
try:
    num = int(input("Enter a number: "))

    if num > 0:
        print("Positive")

    elif num < 0:
        print("Negative")

    else:
        print("Zero")

except ValueError:
    print("Invalid input")
