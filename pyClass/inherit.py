#!/bin/python

from datetime import date

class Person():
  gender = ""

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def calcBirthYear(cls, name, birthYear, extra=""):
    return cls(name, date.today().year - birthYear, extra)

  def __str__(self):
    return f"name: {self.name}, age: {self.age}"

class Man(Person):
  def __init__(self, name, age, voice):
    super().__init__(name, age)
    self.voice = voice

  def __str__(self):
    string = super().__str__()
    return f"{string}, voice: {self.voice}"

man1 = Man.calcBirthYear("abdo", 22, "strong")
man2 = Man("Saad", 13, "Strong")

print(man1)
print(isinstance(man1, Man))
print(man2)
