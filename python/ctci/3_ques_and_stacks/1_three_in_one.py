"""
Implement three stacks using just one arrary
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
from stack import StackEmptyError, StackFullError

def array_of_size(size):
  array = [None] * size
  return array

class FixedSizeStack:
  def __init__(self, array, start, end):
    self.array = array
    self.start = start
    self.end = end
    self.size = 0
  
  def push(self, data):
    ix = self.start + self.size
    if ix > self.end:
      raise StackFullError()
    self.array[ix] = data
    self.size += 1

  def pop(self):
    if self.size == 0:
      raise StackEmptyError()
  
    ix = self.start + self.size - 1
    value = self.array[ix]
    self.array[ix] = None
    self.size -= 1
    return value

def print_array(array):
  r =''
  for i in range(len(array)):
    if array[i] is None:
      r += '_,'
    else:
      r += str(array[i]) + ','
    if i > 0 and (i + 1) % 10 == 0:
      r = r[0:-1]
      r+='|'
  print('[',r[0:-1],']')

if __name__ == "__main__":
  array = array_of_size(30)
  stack_1 = FixedSizeStack(array, 0, 9)
  stack_2 = FixedSizeStack(array, 10, 19)
  stack_3 = FixedSizeStack(array, 20, 29)
  print_array(array)
  stack_1.push(0)
  stack_2.push(10)
  stack_3.push(20)
  print_array(array)
  stack_1.push(1) 
  stack_1.push(2)
  stack_1.push(3)
  stack_1.push(4)
  stack_1.push(5)
  stack_1.push(6)
  stack_1.push(7)
  stack_1.push(8)
  stack_1.push(9)
  print_array(array)
  try:
    stack_1.push(10)
  except StackFullError:
    print("s1 stack is full")
  
  stack_2.pop()
  try:
    stack_2.pop()
  except StackEmptyError:
    print("s2 stack is empty")