import unittest

class Node:
  n = None
  data = None
  def __init__(self, data):
    self.data = data
    self.n = None

  def toStr(self):
    return str(self.data)

  def addToTail(self, d):
    new = self
    while new.n is not None:
      new = new.n
    new.n = Node(d)
    return new.n

  def delete(self, d):
    node = self
    prev = self
    while node is not None:
      if node.data == d:
        break
      prev = node
      node = node.n
      
    val = node.data
    del prev.n
    if node.n is not None:
      prev.n = node.n
    # del node
    return val

class SingleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def addToTail(self, d):
    if self.head is None:
      self.head = Node(d)
      self.tail = self.head
    else:
      self.tail = self.tail.addToTail(d)
  
  def __str__(self):
    r = ''
    node = self.head
    while node is not None:
      r += node.toStr() + ','
      node = node.n
    return r

def printNode(msg, node):
  r = ''
  new = node
  while new is not None:
    r += new.toStr() + '-'
    new = new.n
  print(msg, r)

class Test(unittest.TestCase):
  
  def test_single(self):
     node = Node(5)
     self.assertEquals(5, node.data)
    

if __name__ == "__main__":
  print(': ' * 10)
  node = Node(5)
  printNode('Head: ', node)
  node2 = node.addToTail(10)
  node3 = node.addToTail(15)
  printNode('Head after 15: ',node)
  printNode('Node2 after inserting: ', node2)
  node.delete(15)
  printNode('Head after deleting 15: ',node)
  node2.addToTail(20)
  printNode('Head after 20: ',node)
  node.delete(10)
  printNode('Head after deleting: ',node)

  print('^ ' * 10)
  singleLinkedList = SingleLinkedList()
  print('head: ', singleLinkedList.head)
  singleLinkedList.addToTail(20)
  print('List: ', singleLinkedList)
  singleLinkedList.addToTail(30)
  singleLinkedList.addToTail(40)
  print('List: ', singleLinkedList)
  print('Head: ', singleLinkedList.head.toStr())
  print('Tail: ', singleLinkedList.tail.toStr())
