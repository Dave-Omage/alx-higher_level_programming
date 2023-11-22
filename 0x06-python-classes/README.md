0x06. Python - Classes and Objects

0-square.py - An empty class Square that defines a square
1-square.py - A  class Square that defines a square by: (based on 0-square.py)
2-square.py - A class Square that defines a square by: (based on 1-square.py)
3-square.py - A class Square that defines a square by: (based on 2-square.py)
4-square.py - A class Square that defines a square by: (based on 3-square.py)
5-square.py - A  class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module

