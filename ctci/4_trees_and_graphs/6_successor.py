"""
Find the next value in a BST
"""

from tree_common import * 

minint = -9999999
maxint = 9999999

def succesor(root:TreeNode):
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

def left_most_node(n:TreeNode):  
  if not n:
    return None
  
  while n.left:
    n = n.left
  return n

def sucessor_2(root:TreeNode):
  if not root:
    return None
  if root.right:
    return left_most_node(root.right)
  else:
     q = root
     p = q.parent
     while p and p.left is not q:
       q = p
       p = p.parent
     return p


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