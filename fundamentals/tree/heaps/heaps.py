from binary_tree import Node, insert, inOrderTraversal

class Node:
  def __init__(self, data, parent = None):
    self.left = None
    self.right = None
    self.parent = parent
    self.data = data

def max_heap(node, value):
  if node is None:
    return Node(value)
  
  new = insert_at_bottom(node, value)
  while new.parent is not None:
    parent = new.parent    
    if new.data < parent.data:
      break
    else:
      # swap
      temp = parent.data
      parent.data = new.data
      new.data = temp
      new = parent

def insert_at_bottom(node, value):
  children = [node]
  for i in children:  
    if i.left is None:
      i.left = Node(value, i)
      return i.left
    else:
      children.append(i.left)
    if i.right is None:    
      i.right = Node(value, i)
      return i.right
    else:
      children.append(i.right)

if __name__ == "__main__":
  root = max_heap(None, 35)
  inOrderTraversal(root)
  print('...' * 50)
  max_heap(root, 33)
  inOrderTraversal(root)
  print('...' * 50)
  max_heap(root, 42)
  inOrderTraversal(root)
  print('...' * 50)
  max_heap(root, 10)  
  max_heap(root, 14)
  max_heap(root, 19)
  inOrderTraversal(root)
  print('...' * 50)
  max_heap(root, 27)
  max_heap(root, 44)
  max_heap(root, 26)
  max_heap(root, 31)
  inOrderTraversal(root)
  print('...' * 50)
