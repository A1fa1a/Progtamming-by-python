#!/bin/python

from random import randint
import os

correct_guess = randint(1, 10)

def print_choices():
  print("""
      ================
      Guess the number
      ================
  """)
  print("Guess the number between 1 and 10: ", end="")

def check_guess(user_guess):
  if user_guess != correct_guess:
    print("Wrong. try again.")
    input("Press any key to continue...")
  else:
    print("Congratulations! You guessed the correct number")

print_choices()
user_guess = int(input())
check_guess(user_guess)

while user_guess != correct_guess:
  os.system("cls" if os.name == "nt" else "clear")
  print_choices()
  user_guess = int(input())
  check_guess(user_guess)
