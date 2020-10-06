from abc import ABCMeta, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
A larger interface bundled with all methods makes it mandatory for all classes to provide implementation of all the methods even if 
some methods are not relevant to them
'''

class CommunicationDevice():
  @abstractmethod
  def make_calls():
    pass

  @abstractmethod
  def send_sms():
    pass

  @abstractmethod
  def browse_internet():
    pass

class SmartPhone(CommunicationDevice):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

  class LandlinePhone(CommunicationDevice):
    def make_calls():
      #implementation
      pass

    def send_sms():
      #just pass or raise exception as this feature is not supported 
      pass

    def browse_internet():
      #just pass or raise exception as this feature is not supported
      pass
