"""
min heap
"""

class Node:
  def __init__(self, v):
    self.value = v
    self.left = None
    self.right = None

def array_to_tree(arr):
  root  = Node(arr[0])
  for i in range(1, len(arr)):
    # find left most spot to add the children
    queue = [root]
    parent = None
    while queue and not parent:
      n = queue.pop(0)
      if not n.left or not n.right:
        parent = n
        break
      if n.left:
        queue.append(n.left)
      if n.right:
        queue.append(n.right)
    
    if not parent.left:
      parent.left = Node(arr[i])
    elif not parent.right:
      parent.right = Node(arr[i])
  return root

def inOrderVisit(n, l = 1):
  if n:
    inOrderVisit(n.left, l + 1)
    visit(n, l)
    inOrderVisit(n.right, l + 1)

def visit(n, l):
  print(" " * (l * l), n.value)

# heap methods
def heapify(arr, n, i):
  largest = i
  l = i * 2 + 1
  r = i * 2 + 2
  if l < n and arr[l] < arr[largest]:
    largest = l
  if r < n and arr[r] < arr[largest]:
    largest = r
  if largest != i:
    arr[largest], arr[i] = arr[i], arr[largest]
    heapify(arr, n, largest)

def min_heap(arr):  
  n = len(arr)
  start = n // 2 - 1
  for i in reversed(range(start + 1)):
    heapify(arr, n, i)

if __name__ == "__main__":
  array = [8,9,6,10,45,87,62,63,12,44,78,35,0]
  root = array_to_tree(array)
  inOrderVisit(root)
  heap = array.copy()
  min_heap(heap)
  print("{}\n{}".format(array,heap))
  heap_root = array_to_tree(heap)
  inOrderVisit(heap_root)