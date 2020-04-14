import time;


class MyTree:
  __private_variable = None
  public_variable = "Hi ya"
  def __init__(self):
    self.__private_variable = 5

tree = MyTree()
try:
  print("Cant print private variables ", tree.__private_variable)
except AttributeError:
  print("No access to private variables")
print("But we can print public variables ", tree.public_variable)


class Animal:
  def __init__(self):
    self.birth = time.localtime(time.time())
  
  def __str__(self):
    return time.strftime('%e/%B/%Y %H:%M:%S', self.birth) 

class Dog(Animal):
  pass
class Cat(Animal):
  pass

print("Hello dog ", Dog())
print("Hello cat ", Cat())
