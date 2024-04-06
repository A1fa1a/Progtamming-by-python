# /bin/python

from string import ascii_lowercase as letters
import random

words = []
letter = ""
tries = 6
old_guess = ""
hangman = [
         """
     +------+
           |
           |
           |
           |
    _______|__
         """  ,
         """
   +------+
      |  |
         |
         |
         |
 ________|_
         """,
        """
   +------+
      |  |
      0  |
         |
         |
 ________|_
         """,
         """
   +------+
      |  |
      0  |
      |  |
         |
 ________|_
         """,
         """
   +------+
      |  |
      0  |
     /|  |
         |
 ________|_
         """,
         """
   +------+
      |  |
      0  |
     /|\ |
         |
 ________|_
         """,
      """
      You lose!

  +------+
     |  |
     0  |
    /|\ |
    / \ |
 _______|__
      """
]

while len(words) < random.randint(4, 10):
  for i in range(random.randint(3, 8)):
    for j in random.choice(letters):
      letter += j
  words.append(letter)
  letter = ""

pc_choice = random.choice(words)
hint = ["_"] * len(pc_choice)

print(f"\nYou have {tries} tries")
print(f"{' '.join(hint)}, {len(hint)}\n")
print(pc_choice)
print(hangman[0])

while "_" in hint and tries > 0:
  guess = input("Enter your guess for the letter : ").lower()
  if guess in old_guess:
    print("\nYou have already guessed that, try again.")
  else:
    old_guess += guess
    if guess in pc_choice:
      for i in range(len(pc_choice)):
        if pc_choice[i] == guess:
          hint[i] = guess
          print(" ".join(hint))
    else:
      tries -= 1
      print(hangman[6 - tries])
      print(" ".join(hint))
      print(f"\nYou have {tries} tries")
  if hint == list(pc_choice):
    print(
       """
       *******
       You win
       *******
       """
    )
