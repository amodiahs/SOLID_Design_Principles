from abc import ABCMeta, abstractmethod

#Interface Substitution Principle - Incorrect Implementation
class communication_device():
  @abstractmethod
  def make_calls():
    pass

  @abstractmethod
  def send_sms():
    pass

  @abstractmethod
  def browse_internet():
    pass

class smart_phone(communication_device):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

  class land_line_phone(communication_device):
    def make_calls():
      #implementation
      pass

    def send_sms():
      #just pass or raise exception as this feature is not supported 
      pass

    def browse_internet():
      #just pass or raise exception as this feature is not supported
      pass