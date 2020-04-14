"""
Implement a min method in a stack that always returns the minimum value in the stack.
Pop, push and min should have a O(1) time complexity
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
from stack import print_stack

class Node:
  def __init__(self, data):
    self.data = data
    self.nxt = None
    self.min = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new = Node(data)
    if self.top is None or data <= self.top.data:
      new.min = new
    else:
      new.min = self.top.min
    new.nxt = self.top
    self.top = new
    return self.top

  def pop(self):
    node = self.top
    self.top = self.top.nxt
    return node.data

  def min(self):
    return self.top.min.data


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  print('min:      ', stack.min())  
  print('pop:      ', stack.pop())
  print_stack(stack)
  stack.push(7)
  stack.push(4)
  stack.push(5)
  print('min:      ', stack.min())  
  print_stack(stack)
  stack.push(3)
  print('min:      ', stack.min())  
  stack.pop()
  stack.pop()
  stack.pop()
  print('min:      ', stack.min())  