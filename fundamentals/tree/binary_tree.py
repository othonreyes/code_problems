class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


def insert(root, value):
  """
  For a binary search tree
  """
  if root is None:
    return Node(value)
  
  node = root
  parent = None
  new = Node(value)
  while True:
    parent = node
    if value < parent.data:
      node = parent.left
      if node is None:
        parent.left = new
        break
    else:
      node = parent.right
      if node is None:
        parent.right = new
        break

def search(node, value):
  if node is None:
    return None
  
  while node is not None:
    if value == node.data:
      return node
    if value < node.data:
      node = node.left
    else:
      node = node.right
  return None

def deepest_level(node):
  if node is None:
    return -1
  left_level = deepest_level(node.left) + 1
  right_level = deepest_level(node.right) + 1
  if left_level > right_level:
    return left_level
  else:
    return right_level

def inOrderTraversal(node, level = 0):
  if node is not None:
    inOrderTraversal(node.left, level + 1)
    visit(node, level)
    inOrderTraversal(node.right, level + 1)

def preOrderTraversal(node, level = 0):
  if node is not None:
    visit(node, level)
    preOrderTraversal(node.left, level + 1)
    preOrderTraversal(node.right, level + 1)

def postOrderTraversal(node, level = 0):
  if node is not None:
    postOrderTraversal(node.left, level + 1)
    postOrderTraversal(node.right, level + 1)
    visit(node, level)

def visit(node, level, left = True):
  print('  ' * level, node.data)


if __name__ == "__main__":
  root = Node(10)
  root.left = Node(5)
  root.right = Node(15)
  root.left.left = Node(2)
  root.right.left = Node(12)
  root.right.right = Node(18)
  inOrderTraversal(root)
  print('-' * 50)
  preOrderTraversal(root)
  print('-' * 50)
  postOrderTraversal(root)
  print('-' * 50)

  bst = insert(None, 10)
  inOrderTraversal(bst)
  print('.' * 50)
  insert(bst, 5)
  inOrderTraversal(bst)
  print('.' * 50)
  insert(bst, 15)
  inOrderTraversal(bst)
  print('.' * 50)
  insert(bst, 3)
  insert(bst, 8)
  inOrderTraversal(bst)
  print('.' * 50)
  print('-' * 50, "Search")
  print('Should be none: ', search(None, 10))
  print('Should be none: ', search(bst, 10).data)
  print('Should be none: ', search(bst, 5).data)
  insert(bst, 30)
  insert(bst, 50)
  inOrderTraversal(bst)
  print('Should be none: ', search(bst, 30).data)
  print('-' * 50, "Deepest level")  
  print('Level: ', deepest_level(None))
  print('Level: ', deepest_level(Node(1)))
  print('Level: ', deepest_level(root))
  print('Level: ', deepest_level(bst))