"""
Find the next value in a BST
"""

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


def succesor(root:Node):
  if not root:
    return None

  n = root
  while n.parent:
    n = n.parent

  queue = [n]
  while queue:
    n = queue.pop(0)  
    if n.data > root.data:
      return n
    if n.left:
      queue.append(n.left)
    if n.right:
      queue.append(n.right)
  return None
### not tested
if __name__ == "__main__":
  root = insert(None, 4)
  n2 = insert(root, 2)
  n1 = insert(root, 1)
  n3 = insert(root, 3)
  n8 = insert(root, 8)
  n11 = insert(root, 11)
  n7= insert(root, 7)
  inOrderTraversal(root)

  print("Should be 8 ", succesor(root).data)
  print("Should be None ",succesor(n11))
  print("Should be 2 ", succesor(n1).data)
  print("Should be 2 ", succesor(n3).data)