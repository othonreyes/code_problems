# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
"""
Lowest Common Ancestor in a Binary Search Tree.
        20
     8     22
  4   12 
    10  14
LCA of 10 and 14 is 12
LCA of 14 and 8 is 8
LCA of 10 and 22 is 20
LCA of 4 and 14 is 8
"""
from binary_tree import Node, insert, inOrderTraverse

"""
Approach 1:
- have a dearch function that find the node for n1 and n2 and returns a list
  of the visited notes. T O(logn) and S O(logn)
- Then search both values and get 2 lists.
  - if nodes are the same then assign it temporarily to a variable
  - if not then the lca was the last equal value in the list
  - if a list finishes before the other then the lca is the last element of the 
    least
  T: O(n) where n is the size of the list. In practice it would be O(logn)
Approach 2:
  have a function that search for both values at the same time, and receives the
  parent of the node, if it is root then parent is the root.
  The function returns a class with 3 values: the parent node, if the value was
  found and if the lca was found.
  - if node is none return false and none
  - search both sides and get the result
  - if the result is already found then just returns that.
  - if the parent of of one of the result is the current node the current node
    is the lca
  - if not then return the parent of current node and the OR operation of one of
    them resolved.
  
"""

def lca3(node, n1, n2):
  """Approach 3:
    Use the bst properties. if current node is bigger than both values then the
    result is on the left side. Otherwise the solution is on the right side.
    If none of this is true then the solution is the current node
  """
  if not node:
    return None
  value = node.value
  if value > n1 and value > n2:
    return lca3(node.left, n1, n2)
  elif value < n1 and value < n2:
    return lca3(node.right, n1, n2)
  return node

if __name__ == "__main__":
  print('-----', 'Least common ancestor')
  root = insert(None, 20)
  insert(root, 22)
  insert(root, 8)
  insert(root, 4)
  insert(root, 12)
  insert(root, 10)
  insert(root, 14)
  inOrderTraverse(root)
  print('LCA of ', 20, ' and ', 22, ' is: ', lca3(root, 20,22).value)
  print('LCA of ', 10, ' and ', 14, ' is: ', lca3(root, 10, 14).value)
  print('LCA of ', 4, ' and ', 14, ' is: ', lca3(root, 4, 14).value)
