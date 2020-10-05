# Open - Close Principle
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification
'''
This design breaches the Open Closed principle because this class will need modification if 
a). A new apparel type is to be included and 
b). If the discount amount for any apparel changes
'''
from enum import Enum
class Products(Enum):
  SHIRT = 1
  TSHIRT = 2
  PANT = 3

class DiscountCalculator():
  def __init__(self, product_type, cost):
    self.product_type = product_type
    self.cost = cost

  def get_discounted_price(self):
    if self.product_type == Products.SHIRT:
      return self.cost - (self.cost * 0.10)
    elif self.product_type == Products.TSHIRT:
      return self.cost - (self.cost * 0.15)
    elif self.product_type == Products.PANT:
      return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculator(Products.SHIRT, 100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculator(Products.TSHIRT, 100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculator(Products.PANT, 100)
print(dc_Pant.get_discounted_price())
