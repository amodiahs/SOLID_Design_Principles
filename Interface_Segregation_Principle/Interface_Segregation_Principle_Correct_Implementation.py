from abc import ABCMeta, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
Smaller role interfaces are created for each feature and the classes would only extend the required interfaces and implement the
relevant methods
'''

class CallingDevice():
  @abstractmethod
  def make_calls():
    pass

class MessagingDevice():
  @abstractmethod
  def send_sms():
    pass

class InternetbrowsingDevice():
  @abstractmethod
  def browse_internet():
    pass

class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

class LandlinePhone(CallingDevice):
  def make_calls():
    #implementation
    pass
