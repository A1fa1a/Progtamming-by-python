# bin/python

operation = input("Enter the operation to 'binary' or 'decimal' : ").lower()

if operation == "decimal":
  #convert to decimal
  def binary():
    binary = input("Enter a binary number : ")
    binary = binary[::-1]
    decimal = 0

    for i in range(len(binary)):
      decimal += 2 ** i * int(binary[i])

    print(decimal)
  binary()
elif operation == "binary":
  # convert to binary
  def decimal():
    num = int(input("Enter a decimal number : "))
    binary = ""

    if num != 0:
      while num != 0:
        binary = binary + str(num % 2)
        num //= 2

      while len(binary) < 4:
        binary += "0"

      print(binary[::-1])
    else:
      print("0000")
  decimal()
else:
  print(f"'{operation}'is undefined operation")
