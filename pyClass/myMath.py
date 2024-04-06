# /bin/python
# @staticmethod is a utility method

class Math:
  @staticmethod
  def add(x, y):
    return x + y

  @staticmethod
  def add_5(num):
    return num + 5

  @staticmethod
  def add_10(num):
    return num + 10

  @staticmethod
  def pi():
    return 3.14

a = Math.add(5, 10)
b = Math.add_5(a)
c = Math.add_10(b)
print(a, b, c)
