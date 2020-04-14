from node import Node, print_nodes
from collections import Counter

def remove_duplicates_buffer(n):
  seen = Counter()
  prev = n
  while n is not None:
    if seen[n.data] == 0:
      seen[n.data] = 1
      prev = n
    else:
      prev.nxt = n.nxt
    n = n.nxt

# 2->2
def remove_duplicates_no_buffer(n):
  p1 = n
  while p1.nxt is not None:
    p2 = p1.nxt
    while p2.nxt is not None:
      if p2.nxt.data == p1.data:
        p2.nxt = p2.nxt.nxt
      else:
        p2 = p2.nxt
    p1 = p1.nxt


if __name__ == "__main__":
  l1 = Node(1)
  l1.add(2)
  l1.add(3)
  l1.add(1)
  l1.add(2)
  print_nodes(l1)
  remove_duplicates_buffer(l1)
  print_nodes(l1)

  l1 = Node(1)
  l1.add(2)
  l1.add(3)
  l1.add(1)
  l1.add(2)
  remove_duplicates_no_buffer(l1)
  print_nodes(l1)