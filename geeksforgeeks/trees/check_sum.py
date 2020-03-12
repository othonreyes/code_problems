"""
https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/
"""

class Node:
  def __init__(self, v):
    self.left = None
    self.right = None
    self.value = v

def check_sum(n:Node) -> int:
  if not n:
    return 0
  if not n.left and not n.right:
    return n.value
  if (check_sum(n.left) + check_sum(n.right)) == n.value:
    return n.value
  return -1

def check_sum_root(root:Node) -> bool:
  if not root:
    return False
  val = check_sum(root)
  if val != root.value:
    return False
  return True

if __name__ == "__main__":
  root = Node(10)
  root.left = Node(8)
  root.left.left = Node(3)
  root.left.right = Node(5)
  root.right = Node(2)
  root.right.right = Node(2)
  print(check_sum_root(root))

  root = Node(10)
  root.left = Node(8)
  root.left.left = Node(11)
  root.left.right = Node(5)
  root.right = Node(2)
  root.right.right = Node(2)
  print(check_sum_root(root))