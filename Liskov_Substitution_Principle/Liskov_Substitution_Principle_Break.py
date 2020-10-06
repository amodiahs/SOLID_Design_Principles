# Liskov Substitution Principle
# Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program 
'''
As we can see here, we are trying to loop through a list of car objects. And here we break the Liskov Substitution principle as 
we cannot replace Super type Car’s objects with objects of Sub type PetrolCar in the function written to find Red cars. 
'''

class Car():
  def __init__(self, type):
    self.type = type

class PetrolCar(Car):
  def __init__(self, type):
    self.type = type

car = Car("SUV")
car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}

petrol_car = PetrolCar("Sedan")
petrol_car.properties = ("Blue", "Manual", 4)

cars = [car, petrol_car]

def find_red_cars(cars):
  red_cars = 0
  for car in cars:
    if car.properties['Color'] == "Red":
      red_cars += 1
  print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)
