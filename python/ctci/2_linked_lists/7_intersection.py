# find the intersaction of 2 linked lists
from node import Node, print_nodes, print_node_mem

# Option 1: recursive solution
# get the size of both lists
# in the list that is larger, move n nodes until the rest of the list has the same size as the shorter list
# then recursively compares nodes until they don't match
def intersection(l1, l2):
  size_1 = get_size(l1)
  size_2 = get_size(l2)
  
  n1 = l1
  n2 = l2
  if size_1 > size_2:
    n1 = move(n1, size_1-size_2)
  elif size_1 < size_2:
    n2 = move(n2, size_2 - size_1)
  
  return iter(n1,n2)

def iter(n1, n2):
  if n1 is None and n2 is None:
    return None
  result = iter(n1.nxt, n2.nxt)
  if n1 == n2:
    return n1
  else:
    return result
  
def get_size(n):
  count = 0
  while n is not None:
    n = n.nxt
    count += 1
  return count

def move(n, iterations):
  for _ in range(iterations):
    n = n.nxt
  return n

# Option 2: loop solution
# get the size of both lists and the tails
# If tails don't match return None. Otherwise, move on.
# In the list that is larger, move n nodes until the rest of the list has the same size as the shorter list
# iterate both nodes until they don't match 

class ResultWithTails:
  def __init__(self, tail, size):
    self.tail = tail
    self.size = size

def get_size_with_tails(n):
  count = 1
  while n.nxt is not None:
    count += 1
    n = n.nxt
  return ResultWithTails(n, count)

def intersection2(l1, l2):
  r1 = get_size_with_tails(l1)
  r2 = get_size_with_tails(l2)

  if r1.tail != r2.tail:
    return None

  n1 = l1
  n2 = l2
  if r1.size > r2.size:
    n1 = move(n1, r1.size-r2.size)
  elif r1.size < r2.size:
    n2 = move(n2, r2.size-r1.size)
  
  while n1.nxt is not None and n2.nxt is not None:
    if n1 == n2:
      return n1
    n1 = n1.nxt
    n2 = n2.nxt
  return None

if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  inter = l1.add(3)
  l1.add(4)
  l1.add(5)

  l2 = Node(10)
  l2.add(20)
  l2.add(30)
  inter_2 = l2.add(40)
  inter_2.join(inter)
  print('-' * 50)
  print_node_mem(l1)
  print()
  print('-' * 50)
  print_node_mem(l2)
  print()
  print('-' * 50)
  inter_node = intersection(l1, l2)
  print(inter_node, '-', inter_node.data)
  print('*' * 50)
  inter_node = intersection2(l1, l2)
  print(inter_node, '-', inter_node.data)