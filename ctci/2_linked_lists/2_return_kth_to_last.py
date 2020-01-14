"""
return k to last
Input:1->2->3->4 - k=2
output: 3>4
"""
from node import Node, print_nodes, get_size
from collections import Counter

def return_k_to_last(n, k):
  size = get_size(n)
  for _ in range(size-k):
    n = n.nxt
  return n

class Result:
  def __init__(self, n, k, found):
    self.n = n
    self.k = k
    self.found= found

def return_k_to_last_recursive(n, k):
  if n is None:
    return Result(None, 0, False)
  result = return_k_to_last_recursive(n.nxt, k)
  if result.found:
    return result
  if result.k + 1 == k:
    return Result(n, result.k + 1, True)
  return Result(n, result.k + 1, False)

def return_k_to_last_2(n, k):
  return return_k_to_last_recursive(n, k).n

if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  l1.add(3)
  l1.add(1)
  l1.add(2)  
  print_nodes(return_k_to_last(l1, 2))
  print_nodes(return_k_to_last_2(l1, 2))
