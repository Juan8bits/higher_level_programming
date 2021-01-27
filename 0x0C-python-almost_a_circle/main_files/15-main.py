#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square
if __name__ == "__main__":

    r1 = Square(10)
    r2 = Rectangle(2, 2)
    r3 = Rectangle(69, 4)
    Rectangle.save_to_file([r1, r2, r3])

    with open("Rectangle.json", "r") as file:
        print(file.read())
