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

#https://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/
"""
        1
    2      3
  4   5      6
"""
def tree_size(node):
  if not node:
    return 0
  # don't forget to optimize, this condition can be removed
  if not node.left and not node.right:
    return 1
  return tree_size(node.left) + tree_size(node.right) + 1

# https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
"""
Max depth of a tree
"""
def depth(node, level = 0):
  if not node:
    return level-1
  return max(depth(node.left, level + 1 ), depth(node.right, level + 1 ))
  

if __name__ == "__main__":
  print('-----', 'minimum value')
  root = Node(20)
  root.left = Node(8)
  root.right = Node(22)
  root.left.left = Node(4)
  root.left.right = Node(12)
  root.left.right.left = Node(10)
  root.left.right.right = Node(14)
  print(find_minimum(root))
  print(minimum_BST(root))
  print('-----'*20)
  print('-----', 'tree_size')
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.right = Node(6)
  print(tree_size(root))
  print('-----'*20)
  print('-----', 'max_depth')
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.right = Node(6)
  print(depth(root))
  print('-----'*20)
  