#Breaking - Liskov Substitution Principle 
class car():
  def __init__(self, type):
    self.type = type

class petrol_car(car):
  def __init__(self, type):
    self.type = type

car = car("SUV")
car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}

petrol_car = petrol_car("Sedan")
petrol_car.properties = ("Blue", "Manual", 4)

cars = [car, petrol_car]

def find_red_cars(cars):
  red_cars = 0
  for car in cars:
    if car.properties['Color'] == "Red":
      red_cars += 1
  print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)