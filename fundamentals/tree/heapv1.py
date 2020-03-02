"""
 - Creates heaps from arrays
 - Given an i position of the array, demonstrates that obtains the parent,
    left child and right child
 - heaps:
    - creates a max_heap/min_heap tree from an array of elements
    - heapifys an array of elements
    - inserts a new node in the heap tree
    - extracts a value
"""

from common import NodeHeap, inOrderTraversal
import logging 

log = logging.getLogger('Console')
log.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(consoleHandler)


def heapify_array_to_tree(items):
  assert len(items) > 0

  node = NodeHeap(items[0], 0)
  for i in range(1, len(items)):
    insert_node(node, items[i], i)
  return node

def insert_node(node, item, i):
  # find the parent taht has the left most position empty
  parent = None
  children = [node]
  while children and not parent:
    n = children.pop(0)
    if not n.left or not n.right:
      parent = n
    else:
      children.append(n.left)
      children.append(n.right)

  # then create the node in any of the children slot available
  if not parent.left:
    parent.left = NodeHeap(item, i)
  else:
    parent.right = NodeHeap(item, i)

def search_i(root, i):
  parent = None
  node = None
  children = [root]
  while children and not node:
    n = children.pop(0)
    if n.i == i:
      node = n
    elif n.left and n.left.i == i:
      node = n.left
      parent = n
    elif n.right and n.right.i == i:
      node = n.right
      parent = n
    else:
      children.append(n.left)
      children.append(n.right)
  left_child = 0 if not node.left else node.left.data
  right_child = 0 if not node.right else node.right.data
  log.info("Node value: {}, position: {}, parent: {}, left: {}, right: {}".format(
    node.data, i, parent.data, left_child, right_child))


def max_heapify_tree(items):
  root = NodeHeap(items[0], 0)
  for i in range(1, len(items)):
    # find the parent that has the left most child empty
    log.info("Inserting [{}]= {}".format(i, items[i]))

    parent = None
    children=[root]
    while children and not parent:
      n = children.pop(0)
      if not n.left or not n.right:
        parent = n
      else:
        children.append(n.left)
        children.append(n.right)

    # add the node to the left most position
    n = NodeHeap(items[i], i, parent)
    if not parent.left:
      parent.left = n
    elif not parent.right:
      parent.right = n

    # bubble the value up until the root is the largest element
    while n.parent:
      parent = n.parent
      if parent.data > n.data:
        break
      else:
        parent.data, n.data = n.data, parent.data
        n = parent
  return root

def max_heap_insert_tree(root: NodeHeap, i:int, data: int) -> None:
  # find the parent with the left most child empty
  children = [root]
  parent = None
  while children and not parent:
    n = children.pop(0)
    if not n.left or not n.right:
      parent = n
      break
    if n.left:
      children.append(n.left)
    if n.right:
      children.append(n.left)
  
  # add the node to left if available otherwise to the right
  log.info("Top left node {} ".format(parent.data))
  node = NodeHeap(data, i, parent)
  if not parent.left:
    parent.left = node
  else:
    parent.right = node

  # validate that the max heap is consistent
  while node.parent:
    parent = node.parent
    if parent.data > node.data:
      break
    else:
      # swap values
      parent.data, node.data = node.data, parent.data
      node = parent 


def max_heapify_array(items):
  n = len(items)
  start = n//2 - 1
  for i in reversed(range(0, start+1)):
    log.info('%d', i)
    max_heapify_array2(items, n, i)

def max_heapify_array2(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  if l < n and arr[l] > arr[largest]:
    largest = l
  if r < n and arr[r] > arr[largest]:
    largest = r
  if largest != i:
    arr[largest], arr[i] = arr[i], arr[largest]
    max_heapify_array2(arr, n, largest)



if __name__ == "__main__":
  items = [1,12,9,5,6,10, 13 ,8 ,59, 63, 45]
  root = heapify_array_to_tree(items)
  inOrderTraversal(root)
  i = 2
  search_i(root, i)
  log.info("Parent: (i-1)/2=%d",  items[(i-1)//2])
  log.info("left child: 2i+1=%d",  items[ 2 * i + 1])
  log.info("right child: 2i+2=%d",  items[ 2 * i + 2])

  max_heap_tree = max_heapify_tree(items)
  inOrderTraversal(max_heap_tree)
  
  #### creates a max heap for an array
  items2 = [1,12,9,5,6,10, 13 ,8 ,59, 63, 45]
  log.info(items2)
  max_heapify_array(items2)
  log.info(items2)
  
  # creates a heap for an array 
  root2 = heapify_array_to_tree(items2)
  inOrderTraversal(root2)

  #### inserts a node to a max_heap array
  items2.append(90)
  log.info(items2)
  n2 = len(items2)

  parent = (n2-1) // 2
  log.info("parent: {}, n2 = {}".format(parent, n2))
  max_heapify_array2(items2, n2, parent)
  log.info(items2)

  parent = (5-1) // 2
  log.info("parent: {}, n2 = {}".format(parent, n2))
  max_heapify_array2(items2, n2, parent)
  log.info(items2)

  parent = (2-1) // 2
  log.info("parent: {}, n2 = {}".format(parent, n2))
  max_heapify_array2(items2, n2, parent)
  log.info(items2)

  root2 = heapify_array_to_tree(items2)
  inOrderTraversal(root2)
  #### inserts a node to a tree heap
  log.info("inserts a node to a tree heap")
  max_heap_insert_tree(max_heap_tree, len(items), 90)
  inOrderTraversal(max_heap_tree)