#!/bin/python

from abc import ABC, abstractmethod

class Stream(ABC):
  @abstractmethod
  def read_data(self):
    pass

class FileStream(Stream):
  def __init__(self, file_name):
    self.file_name = file_name

  def read_data(self):
    file = open(self.file_name)
    print(file.read())

file_stream = FileStream(input("Enter the file name: "))
file_stream.read_data()
