"""
Sort a stack. You can use another stack but no other data structure
"""

from stack import Node, Stack, print_stack

# O(n^2)
def sort_stack(stack):  
  sort(stack, Stack(), -1)
  
def sort(stack, buffer, size):
  count = 0
  keep_going = True
  while keep_going:
    val_stack = stack.pop()
    if not buffer.is_empty() and buffer.peek() > val_stack:
      temp = buffer.pop()
      buffer.push(val_stack)
      buffer.push(temp)
    else:        
      buffer.push(val_stack)
    count += 1
    # Update condition
    if size == -1:
      keep_going = not stack.is_empty()
    else:
      keep_going = count < size
  if size == -1:
    size = count
  load(buffer, stack)
  if size == 2:
    load(buffer, stack)
    return
  sort(stack, buffer, size-1)

def load(source, target):
  while not source.is_empty():
    target.push(source.pop())

def sort2(stack):
  buffer = Stack()
  while not stack.is_empty():
    tmp = stack.pop()
    while not buffer.is_empty() and buffer.peek() > tmp:
      stack.push(buffer.pop())
    buffer.push(tmp)
  
  while not buffer.is_empty():
    stack.push(buffer.pop())

if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(8)
  stack.push(4)
  stack.push(7)
  print_stack(stack)
  sort_stack(stack)
  print_stack(stack)

  stack = Stack()
  stack.push(1)
  stack.push(8)
  stack.push(4)
  stack.push(7)
  print_stack(stack)
  sort2(stack)
  print_stack(stack)