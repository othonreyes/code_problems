"""
Tree:
 - insert
 - search
 - inOrderTraverse
 - postOrderTraverse
 - preOrderTraverse
"""

class Node:
  def __init__(self, value, parent = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent


def max_heap(root, value):
  if root is None:
    return Node(value)
  
  node = insert_node(root, value)
  parent = None
  while node.parent is not None:
    parent = node.parent
    if node.value < parent.value:
      return 
    else: 
      parent.value, node.value = node.value, parent.value
      node = node.parent
  return root

def insert_node(node, value):
  children = [node]
  for i in children:
    if i.left is None:
      new = Node(value, i)
      i.left = new
      return new
    else:
      children.append(i.left)
    if i.right is None:
      new = Node(value, i)
      i.right = new
      return new
    else:
      children.append(i.right)

def min_heap(root, value):
  if root is None:
    return Node(value)
  
  node = insert_node(root, value)  
  while node.parent is not None:
    parent = node.parent
    if node.value > parent.value:
      break
    else:
      parent.value, node.value = node.value, parent.value
      node = parent
  return root

def extract_min(root):
  assert root is not None
  # find the bottomost rightmost node
  node = find_bottomost_rightmost_node(root)
  # swap it
  value = root.value
  parent = node.parent
  if parent is not None:
    root.value = node.value
    if parent.left is not None and parent.left.value == root.value:
      parent.left = None
    else:
      parent.right = None
    node.parent = None
    del node
  # bubble down the node
  node = root
  while node.left is not None or node.right is not None:
    left = node.left
    right = node.right
    if left is not None and node.value > left.value:
      node.value, left.value = left.value, node.value
      node = node.left
    else:
      node.value, right.value = right.value, node.value
      node = node.right
  return value
  

def find_bottomost_rightmost_node(node):
  children = [node]
  for i in children:
    if i.left is None and i.right is None:
      return i
    if i.right is None:
      children.append(i.left)
    else:
      if i.left is not None and (i.left.left is not None or i.left.right is not None):
        children.append(i.left)
      else:
        children.append(i.right)
    

    

def inOrderTraverse(node, level = 0):
  if node is not None:    
    inOrderTraverse(node.left, level + 1)
    visit(node, level)
    inOrderTraverse(node.right, level + 1)

def visit(node, level):
  assert node is not None
  print('--' * level, node.value)

if __name__ == "__main__":
  root = max_heap(None, 50)
  max_heap(root, 25)
  max_heap(root, 75)
  max_heap(root, 15)
  max_heap(root, 80)
  max_heap(root, 40)
  max_heap(root, 13)
  max_heap(root, 56)
  max_heap(root, 60)
  max_heap(root, 76)
  inOrderTraverse(root)
  print('..' * 50)
  root = min_heap(None, 50)
  min_heap(root, 25)
  min_heap(root, 75)
  min_heap(root, 15)
  min_heap(root, 80)
  min_heap(root, 40)
  min_heap(root, 13)
  min_heap(root, 56)
  min_heap(root, 60)
  min_heap(root, 76)
  inOrderTraverse(root)
  print('..' * 50)
  root = min_heap(None, 13)
  min_heap(root, 20)
  min_heap(root, 50)
  min_heap(root, 30)
  min_heap(root, 35)
  inOrderTraverse(root)
  print('extract_min: ', extract_min(root))
  inOrderTraverse(root)