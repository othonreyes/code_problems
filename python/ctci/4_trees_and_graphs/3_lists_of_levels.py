from tree_common import TreeNode, insert, inOrderTraversal

from typing import List
from ...fundamentals.linked_lists.single_list import Node as LinkedNode
"""
Use Created linked lists from a tree


"""

def tree_to_linked_lists(root:TreeNode) -> List[LinkedNode]:
  result = [LinkedNode]
  level_to_linked_list(root, result, 0)
  return result

def level_to_linked_list(root:TreeNode, result:List[LinkedNode], level:int):
  if not root:
    return
  
  if len(result) == level:
    result.append([LinkedNode(root)])
  else:
    singly_node = result[level]
    while singly_node.n:
      singly_node = singly_node.n
    singly_node.next = LinkedNode(root)
  level_to_linked_list(root.left, result, level + 1)
  level_to_linked_list(root.right, result, level + 1)

def bst(root):
  if not root:
    return []
  result = [LinkedNode]
  singly_node = LinkedNode(root)

  while singly_node:
    result.append(singly_node)
    parents = singly_node

    prehead = LinkedNode(-1)
    singly_node = prehead
    while parents:
      if parents.data.left:
        singly_node.next = LinkedNode(parents.data.left)
        singly_node = singly_node.next
      if parents.data.right:
        singly_node.next = LinkedNode(parents.data.right)
        singly_node = singly_node.next
    singly_node = prehead.next
  return result


### not tested
if __name__ == "__main__":
  root = insert(None, 4)
  n2 = insert(root, 2)
  n1 = insert(root, 1)
  n3 = insert(root, 3)
  n8 = insert(root, 8)
  n11 = insert(root, 11)
  n7= insert(root, 7)
  tree_to_linked_lists(root)

  