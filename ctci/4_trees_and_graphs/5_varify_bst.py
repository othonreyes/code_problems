from tree_common import * 

"""
Verify that a tree is a BST
"""
minint = -9999999
maxint = 9999999

def is_bst(n:Node, min = minint, max = maxint) -> bool:
  if not n:
    return True
  if n.data < min or n.data > max:
    return False
  return is_bst(n.left, min, n.data) and \
    is_bst(n.right, n.data, max)

### not tested
if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.left.left = Node(1)
  root.left.right = Node(6)
  root.right = Node(8)
  root.right.right = Node(11)
  root.right.left = Node(7)
  print(is_bst(root))
  
  root = Node(4)
  root.left = Node(2)
  root.left.left = Node(1)
  root.left.right = Node(3)
  root.right = Node(8)
  root.right.right = Node(11)
  root.right.left = Node(7)
  print(is_bst(root))