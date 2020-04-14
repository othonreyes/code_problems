## https://www.geeksforgeeks.org/check-sum-covered-uncovered-nodes-binary-tree/


from binary_tree import Node, inOrderTraverse

def sum(n):
  if not n:
    return 0
  return n.value + sum(n.left) + sum(n.right)

def uncovered(root):
  return root.value + searchLeft(root.left) + searchRight(root.right)

def isUncoveredEqualToCovered(root):
  uncoveredSum = uncovered(root)
  total = sum(root)
  covered = total - uncoveredSum
  return covered == uncoveredSum

def searchLeft(n):
  if not n:
    return 0
  value = 0
  if not n.left :
    value = searchLeft(n.right)
  else :
    value = searchLeft(n.left)
  return n.value + value

def searchRight(n):
  if not n:
    return 0
  value = 0
  if not n.right :
    value = searchRight(n.left)
  else :
    value = searchRight(n.right)
  return n.value + value

if __name__ == "__main__":
  root = Node(9)
  root.left = Node(4)
  root.left.left = Node(3)
  root.left.right = Node(6)
  root.left.right.left = Node(5)
  root.left.right.right = Node(7)
  root.right = Node(17)
  root.right.right = Node(22)
  root.right.right.left = Node(20)
  inOrderTraverse(root)
  print(sum(root))
  print(uncovered(root))
  print(isUncoveredEqualToCovered(root))