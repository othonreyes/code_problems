"""
Tree:
 - insert
 - search
 - inOrderTraverse
 - postOrderTraverse
 - preOrderTraverse
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def insert(node, value):
  if node is None:
    return Node(value)
  
  parent = None
  while True:
    parent = node
    if parent.value < value:
      node = parent.left
      if node is None:
        parent.left = Node(value)
        break
    else: 
      node = parent.right
      if node is None:
        parent.right = Node(value)
        break

def search(node, value):
  if node is None:
    return None
  
  while node is not None:
    if node.value == value:
      return node
    if node.value < value:
      node = node.left
    else:
      node = node.right
  return None

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

if __name__ == "__main__":
  root = insert(None, 50)
  inOrderTraverse(root)
  preOrderTraverse(root)
  postOrderTraverse(root)
  insert(root, 25)
  insert(root, 10)
  insert(root, 37)
  insert(root, 44)
  insert(root, 18)
  insert(root, 60)
  insert(root, 73)
  insert(root, 88)
  print('...' * 50)
  inOrderTraverse(root)
  print('...' * 50)
  preOrderTraverse(root)
  print('...' * 50)
  postOrderTraverse(root)
  print('...' * 50)
  print('Search', search(root, 88).value)