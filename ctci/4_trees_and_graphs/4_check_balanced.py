"""

Check if a binary tree is balanced i.e. the difference of the height between 
left and right subtrees is no more than 1
"""


from tree_common import * 

def is_balanced(n:Node) -> bool:
  if not n:
    return False
  _, result = is_tree_balanced(n, 1)
  return result

def is_tree_balanced(n: Node, level: int):
  if not n:
    return level - 1, True
  if not n.left and not n.right:
    return level, True
  l_height, l_balanced = is_tree_balanced(n.left, level + 1)
  r_height, r_balanced = is_tree_balanced(n.right, level + 1)
  if not l_balanced or not r_balanced:
    return level, False
  if abs(l_height - r_height) > 1:
    return level, False
  return max(l_height, r_height), True

### not tested
if __name__ == "__main__":
  root = Node(4)
  assert True == is_balanced(root), "One node should be balanced"  

  root.left = Node(2)
  assert True == is_balanced(root), "One node, one child should be balanced"

  root.left.left = Node(1)
  assert False == is_balanced(root), "One node, with 2 levels child should not be balanced"

  root.right = Node(8)
  assert True == is_balanced(root), "One node, with 2 children and 1 grandchildren should be balanced"
  