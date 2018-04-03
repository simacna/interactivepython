class Person:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  @property
  def full_name(self):
    return self.first + " " + self.last
  @full_name.setter
  def full_name(self, value):
    first,last = value.split()
    self.first = first
    self.last = last

guy = Person("joe", "smith")
# print(guy.full_name)

guy.full_name = "sina sima"
# print(guy.full_name)
guy.full_name = "Sam Jones"
# print(guy.last + ', ' + guy.first)

class Ticket:
  def __init__(self, price):
    self._price = price #protected variable - underscore
    #variable cannot be accessed outside the getter function
    #_ not optional because it means it's internal in python

  @property #getter in order to make a read only variable

  def price(self):
    return self._price 

  @price.setter #allows changing the price of ticket for
  #tickets over $0
  def price(self, new_price):
    #only allow positive prices
    if new_price < 0:
      raise ValueError("nice try")
    self._price = new_price



ticket = Ticket(42)
# ticket.price = 41 - will throw error
# print(ticket.price)
# print(t.price)
#this one wants to use 'update'
class SubscriberOne:
  def __init__(self, name):
    self.name = name

  def update(self, message):
    print('{} got message "{}"'.format(self.name, message))

#this one wants to use 'receive'
class SubscriberTwo:
  def __init__(self, name):
    self.name = name
  def receive(self, message):
    print('{} got message "{}"'.format(self.name, message))



class Publisher:
  def __init__(self):
    self.subscribers = dict()
  def register(self, who, callback=None):
    if callback is None: 
      callback = who.update
      self.subscribers[who] = callback 
  def dispatch(self, message):
    for callback in self.subscribers.values(): 
      callback(message)
  def unregister(self, who): del self.subscribers[who]

