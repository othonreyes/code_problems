class Node:
  def __init__(self, value):
    self.left = self.right = None
    self.value = value

def insert(root, value):
  if not root:
    return Node(value)
  
  if value <= root.value:
      root.left = insert(root.left, value)
  else:
      root.right = insert(root.right, value)
  return root
