# Liskov Substitution Principle
# Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program
'''
A better way to implement this would be to introduce setter and getter methods in the Super class Car using which we can set and 
get Car’s properties without leaving that implementation to individual developers. This way we just get the properties through a 
setter method and its implementation remains internal to the Super class. 
'''
class Car():
  def __init__(self, type):
    self.type = type
    self.car_properties = {}
  
  def set_properties(self, color, gear, capacity):
    self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

  def get_properties(self):
    return self.car_properties

class PetrolCar(Car):
  def __init__(self, type):
    self.type = type
    self.car_properties = {}

car = Car("SUV")
car.set_properties("Red", "Auto", 6)

petrol_car = PetrolCar("Sedan")
petrol_car.set_properties("Blue", "Manual", 4)

cars = [car, petrol_car]

def find_red_cars(cars):
  red_cars = 0
  for car in cars:
    if car.get_properties()['Color'] == "Red":
      red_cars += 1
  print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)
