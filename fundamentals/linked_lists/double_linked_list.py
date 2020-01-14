class Node:
  def __init__(self, data):
    self.n = None
    self.p = None
    self.data = data

  def __str__(self):
    p = '[' if self.p is None else '):'
    nex = ']' if self.n is None else ':('
    return p + str(self.data) + nex

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, d):    
    if self.head is None:
      self.head = Node(d)
      self.tail = self.head
      return self.head
    else:
      new = Node(d)
      self.tail.n = new
      new.p = self.tail
      self.tail = new
      return new
  
  def remove(self, d):
    assert self.head is not None
    node = self.head
    while node.data != d and node.n is not None :
      node = node.n
    if node.data == d:
      val = node.data
      p = node.p
      n = node.n
      if p is not None:
        del p.n #Eraising the node
        p.n = n
      else:
        self.head = n
      if n is not None:
        del n.p
        n.p = p
      else : 
        self.tail = p
      if p is None and n is None:
        self.head = None
        self.tail = None
      return val

  def __str__(self):
    if self.head is None:
      return '[]'
    r = ''
    node = self.head
    while node is not None:
      r += node.__str__()
      node = node.n
    return r

if __name__ == '__main__':
  dll = DoubleLinkedList()
  dll.append(1)
  dll.append(2)
  print(dll)
  dll.append(3)
  print(dll)
  dll.append(4)
  print(dll)
  dll.remove(4)
  print(dll)
  dll.append(5)
  print(dll)
  dll.remove(2)
  print(dll)

  dll2 = DoubleLinkedList()
  dll2.append(1)
  print(dll2)
  dll2.remove(1)
  print(dll2)