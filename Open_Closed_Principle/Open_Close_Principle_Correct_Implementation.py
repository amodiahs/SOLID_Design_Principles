# Open - Close Principle
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification
'''
As shown in this example we have now a very simple base class DiscountCalculator that has a single abstract method get_discounted_price. 
We have created new classes for apparels that extends the base DiscountCalculator class. Hence now every sub class would need to 
implement the discount part on itself. By doing this we have now removed the previous constraints that required modification to the 
base class. Now without modifying the base class we can add more apparels as well as we can change discount amount of an individual 
apparel as needed. 
'''

from enum import Enum
from abc import ABCMeta, abstractmethod

class DiscountCalculator():

  @abstractmethod
  def get_discounted_price(self):
    pass

class DiscountCalculatorShirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculatorTshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())
