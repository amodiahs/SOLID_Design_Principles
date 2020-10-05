# Single Responsibility Principle (aka Separation Of Concerns)
# A class should have only one primary responsibility and reason to change

'''
Let’s take an example of a Telephone Directory application. 
We are designing a Telephone Directory and that contains a TelephoneDirectory Class which is supposed to handle primary responsibility 
of maintaining Telephone Directory entries, i. e Telephone numbers and Names of the entities to which the Telephone Numbers belong. 
Thus, the operations that this class is expected to perform are adding a new entry (Name and Telephone Number), delete an existing entry, 
change a Telephone Number assigned to a particular entity Name, and provide a lookup that returns Telephone Number assigned to a 
particular entity Name.
'''

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

myTelephoneDirectory = TelephoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)

myTelephoneDirectory.delete_entry("Ravi")
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.update_entry("Vikas", 776589)
print(myTelephoneDirectory.lookup_number("Vikas"))
print(myTelephoneDirectory)
