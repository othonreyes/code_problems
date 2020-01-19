# https://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/
"""
      20
    8    22
  4   12
    10   14
"""
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# For BST:
def minimum_BST(node):
  assert node
  while node.left is not None:
    node = node.left
  return node.value

# For any tree
def find_minimum(root):
  if root is None:
    return 100000000
  left = find_minimum(root.left)
  right = find_minimum(root.right)  
  minimum = min(root.value, left, right)
  return minimum
  
if __name__ == "__main__":
  root = Node(20)
  root.left = Node(8)
  root.right = Node(22)
  root.left.left = Node(4)
  root.left.right = Node(12)
  root.left.right.left = Node(10)
  root.left.right.right = Node(14)
  print(find_minimum(root))
  print(minimum_BST(root))