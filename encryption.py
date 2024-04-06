# !/bin/python

import string

alphabet = string.ascii_letters

letter = input("Enter the letter : ")
key = int(input("Enter the key : "))

def encrypt(letter, key):
  encryption = ""

  for i in letter:
    if i not in alphabet:
      encryption += i
    else:
      encryption += alphabet[(alphabet.index(i) + key) % 52]

  return encryption

print(encrypt(letter, key))

quary = input("Enter 'y' to decrypt the letter : ").lower()

def decrypt(code):
  decryption = ""

  for i in code:
    if i not in alphabet:
      decryption += i
    else:
      decryption += alphabet[alphabet.index(i) - key]

  return decryption

if quary == "y":
  print(decrypt(encrypt(letter, key)))
