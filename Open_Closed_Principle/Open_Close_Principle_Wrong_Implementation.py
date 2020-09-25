#Open - Close Principle - Incorrect implementation
from enum import Enum
class products(Enum):
  SHIRT = 1
  TSHIRT = 2
  PANT = 3

class discount_calculator():
  def __init__(self, product_type, cost):
    self.product_type = product_type
    self.cost = cost

  def get_discounted_price(self):
    if self.product_type == products.SHIRT:
      return self.cost - (self.cost * 0.10)
    elif self.product_type == products.TSHIRT:
      return self.cost - (self.cost * 0.15)
    elif self.product_type == products.PANT:
      return self.cost - (self.cost * 0.25)

dc_Shirt = discount_calculator(products.SHIRT, 100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = discount_calculator(products.TSHIRT, 100)
print(dc_TShirt.get_discounted_price())

dc_Pant = discount_calculator(products.PANT, 100)
print(dc_Pant.get_discounted_price())