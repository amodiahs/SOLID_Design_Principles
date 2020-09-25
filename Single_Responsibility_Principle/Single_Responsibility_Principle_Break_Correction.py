# Correction in the code
# To align with Single Responsibility Principle (aka Separation Of Concerns)

class TelephoneDirectory:
  def __init__(self):
    self.telephonedirectory = {}

  def add_entry(self, name, number):
    self.telephonedirectory[name] = number

  def delete_entry(self, name):
    self.telephonedirectory.pop(name)

  def update_entry(self, name, number):
    self.telephonedirectory[name] = number

  def lookup_number(self, name):
    return self.telephonedirectory[name]
 
  def __str__(self):
    ret_dct = ""
    for key, value in self.telephonedirectory.items():
      ret_dct += f'{key} : {value}\n'
    return ret_dct

class persist_to_database:
  #functionality of the class
  def __init__(self, object_to_persist):
    pass

class save_to_file:
  #functionality of the class
  def __init__(self, object_to_save):
    pass

myTelephoneDirectory = TelephoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)

myTelephoneDirectory.delete_entry("Ravi")
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.update_entry("Vikas", 776589)
print(myTelephoneDirectory.lookup_number("Vikas"))
print(myTelephoneDirectory)
