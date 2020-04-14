from tree_common import * 

"""
Use BFS of DFS
- HAve a set for visited to avoid infinite cycles
- if node == target return true
- else  keep checking adjacent nodes
"""

def create_BST(arr: [int]) ->Node:
  return create_min_BST(arr, 0, len(arr) - 1)

def create_min_BST(arr: [int], start:int, end: int) -> Node:
  if start > end:
    return None
  r_i = (start + end) // 2
  root = Node(arr[r_i])
  root.left = create_min_BST(arr, start, r_i - 1)
  root.right = create_min_BST(arr, r_i + 1, end)
  return root

### not tested
if __name__ == "__main__":
  root = create_BST([0,1,2,3,4,5])
  inOrderTraversal(root)
  