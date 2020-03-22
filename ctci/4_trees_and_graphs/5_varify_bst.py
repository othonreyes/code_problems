from tree_common import * 

"""
Verify that a tree is a BST
"""
minint = -9999999
maxint = 9999999

def is_bst(n:TreeNode, min = minint, max = maxint) -> bool:
  if not n:
    return True
  if n.data < min or n.data > max:
    return False
  return is_bst(n.left, min, n.data) and \
    is_bst(n.right, n.data, max)

last_value = None
def in_order_bst(root):
  if not root:
    return True
  if not in_order_bst(root):
    return False
  if not last_value None and last_value > root.value:
    return False
  last_value = root.value
  if not in_order_bst(root.right):
    return False
  return True

### not tested
if __name__ == "__main__":
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(6)
  root.right = TreeNode(8)
  root.right.right = TreeNode(11)
  root.right.left = TreeNode(7)
  print(is_bst(root))
  
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right = TreeNode(8)
  root.right.right = TreeNode(11)
  root.right.left = TreeNode(7)
  print(is_bst(root))