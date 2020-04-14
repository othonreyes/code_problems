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

def inOrderTraverse(node, level = 0):
  if node is not None:    
    inOrderTraverse(node.left, level + 1)
    visit(node, level)
    inOrderTraverse(node.right, level + 1)

def preOrderTraverse(node, level = 0):
  if node is not None:
    visit(node, level)
    preOrderTraverse(node.left, level + 1)
    preOrderTraverse(node.right, level + 1)

def postOrderTraverse(node, level = 0):
  if node is not None:    
    postOrderTraverse(node.left, level + 1)
    postOrderTraverse(node.right, level + 1)
    visit(node, level)

def visit(node, level):
  assert node is not None
  print('--' * level, node.value)
