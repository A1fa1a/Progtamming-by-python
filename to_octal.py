# /bin/python

def to_octal():
  operation = input("Enter '1' decimal to octal\nor '2' octal to decimal\nor '3' octal to binary\nor '4' binary to octal : ")
  result = ""
  grade = 0
  temp = 0
  num = 0

  def matrix(x=0, y=0, items=""):
    a = [[2 for row in range(x)] for col in range(y)]

    for i in range(len(a)):
      for j in range(x):
        a[i][j] = items[i]

    return a

  if operation == "1":
    num = int(input("Enter a number : "))

    while num != 0:
      result += str(num % 8)
      num //= 8

    return result[::-1]
  elif operation == "2":
    octal = input("Enter an octal number : ")
    octal = octal[::-1]
    result = 0

    for i in octal:
      result += 8 ** grade * int(i)
      grade += 1

    return result
  elif operation == "3":
    octal = input("Enter an octal number : ")
    int_octal = int(octal)
    temp = ""

    if int_octal != 0:
      for i in octal:
        i = int(i)
        while i != 0:
          temp += str(i % 2)
          i //= 2
        while len(temp) < 3:
          temp += "0"

        result += temp[::-1]
        temp = ""

    else:
      print("0000")

    return result
  elif operation == "4":
    binary = input("Enter a binary number : ")

    for i in range(len(binary)):
      temp += 2 ** grade * int(binary[i])
      num += 1
      grade += 1
      if num == 3:
        result += str(temp)
        temp = 0
        num = 0
        grade = 0
#        print("Success")

    if result[0] == "0":
      result = result[1::]

    return result

print(to_octal())
