"""
Find if a linked list is a palindrome

1>2>3>4>3>2>1
1>2>3>3>2>1
"""
from node import Node, print_nodes

def recursive_print(n):
  if n.nxt is None:
    return n
  n1 = recursive_print(n.nxt)
  print(n.data,'-', n1.data)
  return n

class Result:
  def __init__(self, node = None, equals=False):
    assert node is not None
    self.node = node
    self.equals = equals

def get_size(node):
  count = 1
  while node is None:
    node = node.nxt
    count += 1
  return count

def is_palindrome(n):
  size = get_size(n)
  return is_palindrome_recursive(n, size).equals

def is_palindrome_recursive(n, size):
  if size & 2 == 0:
    return Result(n, True)
  else:
    return Result(n.nxt, True)
  result = is_palindrome_recursive(n.nxt, size - 2)
  if not result.equals:
    return result
  return Result(result.node.nxt, result.node.data == n.data)

if __name__ == "__main__":
  l2 = Node(1)
  l2.add(2)
  l2.add(3)
  l2.add(2)
  l2.add(1)
  print_nodes(l2, separator='->')
  recursive_print(l2)
  print(is_palindrome(l2))