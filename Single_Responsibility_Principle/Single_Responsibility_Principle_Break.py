# Single Responsibility Principle (aka Separation Of Concerns)
# A class should have only one primary responsibility and reason to change
'''
Now let’s say that there are two more requirements in the project – Persist the contents of Telephone Directory to a 
Database and transfer the contents of Telephone Directory to a file. 
So we can add two more methods to the TelephoneDirectory class as shown in this example.
Now this is where we broke the Single Responsibility Design Principle. By adding the functionalities of persisting to 
database and saving to file, we gave additional responsibilities to TelephoneDirectory class which are not its primary responsibility. 
This class now has additional features that can cause it to change. In future if there are any requirements related to persisting the 
data then those can cause changes to the TelephoneDirectory class. Thus, TelephoneDirectory is prone to changes due to the reasons 
that are not its primary responsibility. 
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
 
  def save_to_file(self, file_name, location):
    #code to save the contents of telephonedirectory dictionary to the file
    pass

  def persist_to_database(self, database_details):
    #code to persist the contents of telephonedirectory dictionary to database
    pass

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
