import logging 

log = logging.getLogger('Console')

ch = filter(lambda h: isinstance(h,logging.StreamHandler), log.handlers)

consoleHandler = None
if ch:
  for i in ch:
    consoleHandler = i

if not consoleHandler:
  log.setLevel(logging.INFO)
  consoleHandler = logging.StreamHandler()
  consoleHandler.name = 'Console'
  consoleHandler.setLevel(logging.INFO)
  consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
  log.addHandler(consoleHandler)



class TreeNode:
  def __init__(self, data, parent = None):
    self.left = None
    self.right = None
    self.parent = parent
    self.data = data

class NodeHeap:
  def __init__(self, data, i, parent = None):
    self.left = None
    self.right = None
    self.parent = parent
    self.data = data
    self.i = i

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
  log.info("{}{}".format('  ' * level, node.data))


def insert(root:TreeNode, value: int)->TreeNode:
  if not root:
    return TreeNode(value)

  n = root
  while True:
    if value < n.data:
      if n.left:
        n = n.left
      else:
        n.left = TreeNode(value, n)
        return n.left
    else:
      if n.right:
        n = n.right
      else:
        n.right = TreeNode(value, n)
        return n.right



