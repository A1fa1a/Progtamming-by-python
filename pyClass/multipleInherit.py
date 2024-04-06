#!/bin/python

class Creature:
  def __init__(self):
    print("From creature class")

  def eat(self):
    print("eat function from creature class")

class Human:
  def __init__(self):
    print("From human class")

  def job(self):
    print("job function from human class")

class Studint(Creature, Human):
  pass

ali = Studint()

ali.eat()
ali.job()
