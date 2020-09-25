#Open - Close Principle - Correct implementation
from enum import Enum
from abc import ABCMeta, abstractmethod

class discount_calculator():

  @abstractmethod
  def get_discounted_price(self):
    pass

class discount_calculator_shirt(discount_calculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.10)

class discount_calculator_tshirt(discount_calculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.15)

class discount_calculator_pant(discount_calculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.25)

dc_Shirt = discount_calculator_shirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = discount_calculator_tshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = discount_calculator_pant(100)
print(dc_Pant.get_discounted_price())