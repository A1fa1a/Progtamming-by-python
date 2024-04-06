# /bin/python

from datetime import date

class Student:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  @classmethod
  def count_age(cls, name, birthyear):
    return cls(name, date.today().year - birthyear)

  def get_name(self):
    return f"The name is {self.__name}"

  def set_name(self, new_name):
    self.__name = new_name


  def get_age(self):
    return f"The age is {self.__age}"

  def set_age(self, new_age):
    self.__age = new_age

student_1 = Student("Abdo", 21)
student_2 = Student.count_age("saad", 2011)

print(f"{student_1.get_name()} and {student_1.get_age()}")
print(f"{student_2.get_name()} and {student_2.get_age()}")


