class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert(root, value):
  if not root:
    root = Node(value)
    return root  
  n = root
  while True:    
    if n.value > value: #go left      
      if  n.left is None:
        n.left = Node(value)
        break
      else: 
        n = n.left
    else:
      if n.right is None:
        n.right = Node(value)
        break
      else: 
        n = n.right

def search(root, value):
  if not root:
    return None
  n = root
  while n:
    if n.value == value:
      return n
    if n.value > value: # search left
      n = n.left
    else:
      n = n.right # search right
  return None

def isCompleteTree(root):
  if not root:
    return False
  
  nodes = [root]
  n = None
  while nodes:
    n = nodes.pop(0)
    if not checkNodeCompleteTree(n):
      return False
    if n:      
      nodes.append(n.left)
      nodes.append(n.right)
  return True


def checkNodeCompleteTree(root):
  if not root:
    return True
  if root.left and root.right:
    return True
  if root.left and not root.right:
    return True
  if not root.left and not root.right:
    return True
  return False

def isFullTree(root):
  if not root:
    return False
  nodes = [root]
  n = None
  while nodes:
    n = nodes.pop(0)
    if not checkNodeForFullTree(n):
      return False
    if n:
      nodes.append(n.left)
      nodes.append(n.right)
  return True

def checkNodeForFullTree(n):
  if not n:
    return True
  if n.left and n.right:
    return True
  if not n.left and not n.right:
    return True
  return False

def inOrderTraversal(root, level= 0):
  if root:
    inOrderTraversal(root.left, level + 1)
    visit(root, level)
    inOrderTraversal(root.right, level + 1)

def preOrderTraversal(root, level= 0):
  if root:
    visit(root, level)
    preOrderTraversal(root.left, level + 1)    
    preOrderTraversal(root.right, level + 1)

def postOrderTraversal(root, level= 0):
  if root:
    visit(root, level)
    postOrderTraversal(root.left, level + 1)    
    postOrderTraversal(root.right, level + 1)

def visit(node, level = 0):
  print(" " * level, node.value)


def make_complete_tree():
  root = Node(1)
  root.left = Node(12)  
  root.left.left = Node(5)
  root.left.right = Node(6)
  root.right = Node(9)
  root.right.left = Node(5)
  return root

def make_complete_tree_and_full_tree():
  root = Node(1)
  root.left = Node(12)  
  root.left.left = Node(5)
  root.left.right = Node(6)
  root.right = Node(9)
  return root

def make_incomplete_tree():
  root = Node(1)
  root.left = Node(12) 
  root.left.left = Node(5)
  root.left.right = Node(6)
  root.right = Node(9)
  root.right.right = Node(8)
  return root

def deepest_level(node, level = 0):
  if not node:
    return level
  return max(deepest_level(node.left, level+1), deepest_level(node.right, level+1))

def print_from_bottom(node):
  """
  Print a tree from the bottom to the top
  """
  max_level = deepest_level(node)
  for i in reversed(range(1, max_level + 1)):
    print_level(node, i, 1)
    print()

def print_level(node, level, current):
  if current == level and node:
    print(node.value, end=",")
    return
  if node.left:
    print_level(node.left, level, current + 1)
  if node.right:
    print_level(node.right, level, current + 1)

def h_in_order(node):
  max_level = deepest_level(node)
  
  n = None
  nodes = [node]
  for i in range(max_level):
    children = []
    while nodes:         
      n = nodes.pop(0)
      print(" " * (max_level - i), n.value, end="")
      children.append(n.left)
      children.append(n.right)
    nodes = children
    print()


if __name__ == "__main__":
  root = insert(None, 27)  
  insert(root, 14)
  insert(root, 35)
  insert(root, 10)
  insert(root, 19)
  insert(root, 31)
  insert(root, 42)
  inOrderTraversal(root)
  print("Search ", search(root, 27).value)
  print("Search ", search(root, 42).value)
  print("Search ", search(root, 90))
  print("Root should be a complete tree ", isCompleteTree(root))
  print("Root should be a complete tree ", isCompleteTree(make_complete_tree()))
  print("Root should be a complete tree ", isCompleteTree(make_complete_tree_and_full_tree()))
  print("Root should not be a complete tree ", isCompleteTree(make_incomplete_tree()))
  print("Root should be a full tree ", isFullTree(root))
  print("Root should NOT be a full tree ", isFullTree(make_complete_tree()))
  print("Root should be a full tree ", isFullTree(make_complete_tree_and_full_tree()))
  print("Root should NOT be a full tree ", isFullTree(make_incomplete_tree()))
  print("deepest_level ", deepest_level(root))
  print_from_bottom(root)
  h_in_order(root)