#!/bin/python

from abc import ABCMeta, abstractmethod

# Example: 1

class Programming(metaclass=ABCMeta):
  @abstractmethod
  def has_oop(self):
    pass

class Python(Programming):
  def has_oop(self):
    return "Yes"

class Pascal(Programming):
  def has_oop(self):
    return "NO"

one = Python()
print(one.has_oop())

two = Pascal()
print(two.has_oop())

# Example: 2

class Animal(metaclass=ABCMeta):
  @abstractmethod
  def __init__(self, name, speed):
    self.name = name
    self.speed = speed

  # You don't need to add this in subclasses and you can use it simply
  def animal_has(self):
    print("Face\nBody\nlegs")

class Cat(Animal):
  def __init__(self, name, speed):
    super().__init__(name, speed)

class Dog(Animal):
  def __init__(self, name, speed):
    super().__init__(name, speed)

cat = Cat("Kiti", 50)
dog = Dog("Rixe", 70)

print(cat.name, cat.speed)
cat.animal_has()
