"""
Implement a set of stacks such as when one stack is full then you create a new stack
and you push the elements there. push and pop operations should function like in regular
stacks.
"""

from stack import Node, print_stack, StackEmptyError, StackFullError

class Stack:
  def __init__(self, limit):
    self.top = None
    self.size = 0
    self.limit = limit
  
  def is_full(self):
    return self.size == self.limit

  def is_empty(self):
    return self.size == 0

  def push(self, data):
    if self.size == self.limit:
      raise StackFullError()
    new = Node(data)
    new.nxt = self.top
    self.top = new
    self.size += 1
  
  def pop(self):
    if self.limit == 0:
      raise StackEmptyError()
    node = self.top
    self.top = self.top.nxt
    self.size -= 1
    return node.data

  def __str__(self):
    r = ''
    i = 1
    n = self.top
    while n is not None:
      if i > self.size:
        r += '_'
      else:
        r += str(n.data)
      n = n.nxt
      i += 1
      r += ','
    return r[0: -1]

MAX_SIZE = 5
class SetOfStacks:
  def __init__(self):
    self.top = None
    self.stacks = []
    self.stacks.append(Stack(MAX_SIZE))
    self.index = 0

  def push(self, data):
    stack = self.stacks[self.index]
    if stack.is_full():
      self.stacks.append(Stack(MAX_SIZE))
      self.index += 1
      stack = self.stacks[self.index]
    stack.push(data)
  
  def pop(self):
    stack = self.stacks[self.index]
    value = stack.pop()
    if stack.is_empty():
      self.stacks[self.index] = None
      self.index -= 1
    return value
  

def print_array(stacks):
  r =''
  for i in range(len(stacks.stacks)):
    stack = stacks.stacks[i]
    r += str(stack) + '|'
  print('[',r[0:-1],']')


if __name__ == "__main__":
  set_stacks = SetOfStacks()
  set_stacks.push(1)
  print_array(set_stacks)
  set_stacks.push(2)
  set_stacks.push(3)
  set_stacks.push(4)
  set_stacks.push(5)
  print_array(set_stacks)
  print('stack 0 is full', set_stacks.stacks[0].is_full())
  set_stacks.push(6)
  print_array(set_stacks)
  set_stacks.pop()
  print_array(set_stacks)
  set_stacks.pop()
  print_array(set_stacks)
  

