#https://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/
"""
        1
    2      3
  4   5      6
"""
from binary_tree import Node

def tree_size(node):
  if not node:
    return 0
  if not node.left and not node.right:
    return 1
  return tree_size(node.left) + tree_size(node.right) + 1

if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.right = Node(6)
  print(tree_size(root))