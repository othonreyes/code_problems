"""
Problem: Implement a queue with 2 stacks
"""

"""
Approach:
On push, keep elements on one stack in the case that the client of the Queue wans to continue pushing data. On pop,
first put all the elements of the "push stack" into the "pop stack", then pop the element. Keep the data in the "pop 
stack" in case that the client wants to continue popping elements. On push, put the elements back first
"""

from stack import Node, Stack, print_stack

class StackedQueue:
  def __init__(self):
    self.push_stack = Stack()
    self.pop_stack = Stack()

  def add(self, data):
    if not self.pop_stack.is_empty():
      self.transfer_data(self.pop_stack, self.push_stack)
    self.push_stack.push(data)

  def remove(self):
    if not self.push_stack.is_empty():
      self.transfer_data(self.push_stack, self.pop_stack)
    return self.pop_stack.pop()

  def transfer_data(self, source, target):
    while not source.is_empty():
      target.push(source.pop())

  def print(self):
    if self.push_stack.is_empty():
      print_stack(self.pop_stack)
    else:
      print_stack(self.push_stack)

if __name__ == "__main__":
  queue = StackedQueue()
  queue.add(1)
  queue.add(2)  
  queue.print()
  print(queue.remove())
  queue.print()