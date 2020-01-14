class StackFullError(Exception):
  def __init__(self):
    self.message = "Can't add new element, it is full"

class StackEmptyError(Exception):
  def __init__(self):
    self.message = "The stack is empty"

class Node:
  def __init__(self, data):
    self.data = data
    self.nxt = None

class Stack:
  def __init__(self):
    self.top = None
    self.count = 0
  
  def push(self, data):
    new = Node(data)
    new.nxt = self.top
    self.top = new
    self.count += 1
    return self.top
  
  def is_empty(self):
    return self.top is None

  def peek(self):
    assert self.top is not None
    return self.top.data
  
  def pop(self):
    assert self.top is not None
    data = self.top.data
    self.top = self.top.nxt
    self.count -= 1
    return data

  def add_many(self, values):
    for i in values:
      self.push(i)

def print_stack(stack):
  r = ''
  n = stack.top
  while n is not None:
    r += str(n.data) + '-'
    n = n.nxt
  print('[',r[:-1],']')

if __name__ == "__main__":
   stack = Stack()
   stack.push(1)
   print('peek:     ', stack.peek())
   print('is_empty: ', stack.is_empty())
   print('pop:      ', stack.pop())
   print('is_empty: ', stack.is_empty())
   stack.add_many([1,2])
   print_stack(stack)
   