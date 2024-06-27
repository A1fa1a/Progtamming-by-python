#!/bin/python

import os

hexa_dict_capital = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
hexa_dict_small = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

def clear_screan():
  os.system("cls" if os.name == "nt" else "clear")

def print_user_choices():
  print("""
   ==========================
   Convert to hexa or deximal\n
   ==========================
  """)
  print("Choice a number to convert to hexa or decimal:")
  print("1- From hexa to decimal.")
  print("2- From decimal to hexa.")
  print("3- Exit")

def is_hexa(num:[list, str]) -> bool:
  hexa_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "b", "c", "d", "e", "f"]

  for i in num:
    if i in hexa_list:
      continue
    else:
      return False
  return True

def is_number(num:[list, str]) -> bool:
  for i in num:
    try:
      int(i)
    except ValueError:
      return False
  return True

def convert_hexa_letters(num:str) -> [str, int]:
  if is_hexa(num) and not is_number(num):
    for key in hexa_dict_capital:
      if hexa_dict_capital[key] == num or hexa_dict_small[key] == num:
        return key
  elif is_number(num) and int(num) > 9 and int(num) < 16:
    return hexa_dict_capital[int(num)]
  else:
    raise ValueError

def to_decimal():
  hexa_num = list(input("Enter a hexadecimal number: "))
  power = len(hexa_num) - 1
  counter = 0
  result = 0

  if is_hexa(hexa_num):
    for num in hexa_num:
      if is_hexa(num) and not is_number(num):
        result += (convert_hexa_letters(num)) * (16 ** (power - counter))
      else:
        result += int(num) * (16 ** (power - counter))
      counter += 1
    print(result)
  else:
    print("Invalid input, enter a hexadecimal number")

def to_hexa():
  decimal_num = int(input("Enter a decimal numner: "))
  result = ""

  while decimal_num != 0:
    if is_number(str(decimal_num)):
      remainder = str(decimal_num % 16)
      if int(remainder) > 9:
        result += str(convert_hexa_letters(remainder))
      else:
        result += remainder
      decimal_num //=16
    else:
      raise ValueError
  index = len(result) - 1
  while index >= 0:
    print(result[index], end="")
    index -= 1

while True:
  print_user_choices()

  try:
    user_choice = int(input())
    if user_choice == 1:
      to_decimal()
    elif user_choice == 2:
      to_hexa()
    elif user_choice == 3:
      print("\nProgram exit...")
      break
    else:
      print(f"'{user_choice}' is not a vaild number")
    input("\nPress enter to continue...")
    clear_screan()
  except ValueError:
    print("Invalid input, please enter a number")
