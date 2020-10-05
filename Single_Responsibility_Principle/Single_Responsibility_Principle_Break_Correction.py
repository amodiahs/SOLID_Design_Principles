# Single Responsibility Principle (aka Separation Of Concerns)
# A class should have only one primary responsibility and reason to change
'''
Single Responsibility Principle asks us not to add additional responsibilities to a class so that we don’t have to modify a class 
unless there is change to its primary responsibility. We can handle the current situation by having separate classes that would 
handle database persistence and saving to file. We can pass the TelephoneDirectory object to the objects of those classes and 
write any additional features in those classes. 
This would ensure that TelephoneDirectory class has only one reason to change that is any change in its primary responsibility
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
