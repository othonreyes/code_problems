"""
Implement a shelter that operates on a "first in- first out basis.
Shelter can dogs or cats and people can say what would they prefer
but they get the oldest of that type or the oldest animal in the shelter.
"""

"""
Approach:
Have to queues one for cats and one for dogs. If one is empty then get an animal
 from the other queue.
"""
from queue import Node, print_queue

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
  
  def enqueue(self, data):
    new = Node(data)
    if self.is_empty():
      self.first = new
      self.last = self.first
    else:
      # new.nxt = self.last.nxt points to nothing
      self.last.nxt = new
      self.last = new
  
  def dequeue(self):
    if self.is_empty():
      return None
    node = self.first
    self.first = self.first.nxt
    return node.data
  
  def is_empty(self):
    return self.first is None
  
  def peek(self):
    if self.is_empty():
      return None
    return self.first.data

class Animal:
  def __init__(self, order):
    self.order = order

class Dog(Animal):
  def __init__(self, order = 0):
    self.order = order
  
  def __str__(self):
    return 'Dog(' + str(self.order) + ')'

class Cat(Animal):
  def __init__(self, order = 0):
    self.order = order

  def __str__(self):
    return 'Cat(' + str(self.order) + ')'

class Shelter:
  def __init__(self):
    self.dogs = Queue()
    self.cats = Queue()
    self.order = 1 

  def enqueue(self, animal):
    if isinstance(animal, Dog):
      self.dogs.enqueue(Dog(self.order))
    else:
      self.cats.enqueue(Cat(self.order))
    self.order += 1

  def dequeueDog(self):
    if self.dogs.is_empty():
      return self.cats.dequeue()
    return self.dogs.dequeue()

  def dequeueCat(self):
    if self.cats.is_empty():
      return self.dogs.dequeue()
    return self.cats.dequeue()

  def dequeueAny(self):
    oldest_dog = self.dogs.peek()
    oldest_cat = self.dogs.peek() 
    if oldest_dog is None or oldest_cat.order > oldest_dog.order:
      return self.cats.dequeue()
    else:
      return self.dogs.dequeue()

  def print(self):
    print_queue(self.dogs, "Dogs:")
    print_queue(self.cats, "Cats:")


if __name__ == "__main__":
  shelter = Shelter()
  shelter.enqueue(Dog())
  shelter.print()
  shelter.enqueue(Dog())
  shelter.enqueue(Cat())
  shelter.print()
  shelter.enqueue(Dog())
  shelter.enqueue(Cat())  
  shelter.enqueue(Cat())
  shelter.enqueue(Dog())
  shelter.enqueue(Cat())
  shelter.print()
  animal = shelter.dequeueAny()
  print(animal)
  cat = shelter.dequeueCat()
  dog = shelter.dequeueDog()
  print(cat, ' ', dog)