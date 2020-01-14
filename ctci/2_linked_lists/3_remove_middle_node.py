"""
return k to last
Input:  1->2->8->5->10 - node = 5
output: 1->2->8->10
"""
from node import Node, print_nodes, get_size
from collections import Counter

def remove_middle(n):
  if n is None or n.nxt is None:
    return
  nxt = n.nxt
  n.data = nxt.data
  n.nxt = nxt.nxt

if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  l1.add(8)
  remove_me = l1.add(5)
  l1.add(10)
  print_nodes(l1)
  remove_middle(remove_me)
  print_nodes(l1)
