#!/bin/python

from abc import ABC, abstractmethod

class shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Square(shape):
  def __init__(self, side):
    self.__side = side

  def area(self):
    return self.__side * self.__side

  def perimeter(self):
    return self.__side * 4

class Rectangle(shape):
  def __init__(self, length, width):
    self.__length = length
    self.__width = width

  def area(self):
    return self.__length * self.__width

  def perimeter(self):
    return self.__length + self.__width * 2

square_1 = Square(10)
rectangle_1 = Rectangle(10, 5)

print(f"sapure => area: {square_1.area()}, perimeter: {square_1.perimeter()}")
print(f"triangle => area: {rectangle_1.area()}, perimeter: {rectangle_1.perimeter()}")
