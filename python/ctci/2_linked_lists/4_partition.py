"""
return k to last
Input: 1->2->8->5->10->5->3->1 partion = 5
output: 1->2->3->1  ->  8->5->10->5 partion = 5
"""
from node import Node, print_nodes, get_size
from collections import Counter

def partition(n, k):
  prev_pointer = None
  while n is not None:
    if n.data < k:
      if prev_pointer is not None:
        temp = prev_pointer.data
        prev_pointer.data = n.data
        n.data = temp
        prev_pointer = prev_pointer.nxt
    else: 
      if prev_pointer is None:
        prev_pointer = n
    n = n.nxt

if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  l1.add(8)
  l1.add(5)
  l1.add(10)
  l1.add(5)
  l1.add(3)
  l1.add(1)
  print_nodes(l1)
  # Input: 1->2->8->5->10->5->3->1 partion = 5
  partition(l1, 5)
  print_nodes(l1)
