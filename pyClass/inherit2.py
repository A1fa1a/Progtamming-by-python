#!/bin/python

class Food:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price

  def getName(self):
    return self.__name

  def getPrice(self):
    return self.__price

  def setName(self, newName):
    self.__name = newName

  def setPrice(self, newPrice):
    self.__price = price

  def __str__(self):
    return f"name: {self.__name}, price: {self.__price}"

class Apple(Food):
  def __init__(self, name, price, color):
    super().__init__(name, price)
    self.__color = color

  def __str__(self):
    string = super().__str__()
    return f"{string}, color: {self.__color}"

food1 = Apple("Apple", 5, "Red")

print(food1)
