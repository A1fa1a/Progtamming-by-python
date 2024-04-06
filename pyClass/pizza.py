# /bin/python

import myMath

class Pizza:
  def __init__(self, ingred, radius):
    self.ingred = ingred
    self.radius = radius

  def area(r):
    return Pizza.circal_radius(self.radius)

  @staticmethod
  def circal_radius(r):
    return r ** 2 * math.pi()

  @classmethod
  def veg(clas):
    return clas(["mashrome", "tomato", "qucamper"], 3)

  @classmethod
  def meat(clas):
    return clas(["meat", "botato"], 4)

  def __str__(self):
    return f"Pizza ingredanse is : {self.ingred}"

pizza_1 = Pizza(["cheese", "onion", "tomato", "pepper"], 6)
pizza_2 = Pizza.veg()
pizza_3 = Pizza.meat()

print(f"{pizza_1}\n{pizza_2}\n{pizza_3}")
