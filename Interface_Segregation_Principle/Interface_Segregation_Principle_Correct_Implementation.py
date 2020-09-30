from abc import ABCMeta, abstractmethod

#interface Substitution Principle - Correct Implementation

class calling_device():
  @abstractmethod
  def make_calls():
    pass

class messaging_device():
  @abstractmethod
  def send_sms():
    pass

class internet_browsing_device():
  @abstractmethod
  def browse_internet():
    pass

class smart_phone(calling_device, messaging_device, internet_browsing_device):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

class land_line_phone(calling_device):
  def make_calls():
    #implementation
    pass