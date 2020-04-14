from tree_common import * 

## Brute force
## Accumulating from the top and exploring each subnode
def total_paths(root: TreeNode, tv:int) -> int:
  if not root:
    return 0
  
  tp = total_paths_from_tree(root, tv, 0)
  tp += total_paths(root.left, tv)
  tp += total_paths(root.right, tv)
  return tp

def total_paths_from_tree(root: TreeNode, tv:int, acc:int) -> int:
  if not root:
    return 0

  tp = 0
  acc += root.data
  if acc == tv:
    tp += 1
  
  tp += total_paths_from_tree(root.left, tv, acc)
  tp += total_paths_from_tree(root.right, tv, acc)
  return tp

# Approach : global variable and accumulating from the bottom
total_paths_global = 0
def total_paths_2(root: TreeNode, tv: int):
  if not root:
    return []

  results:[int] = total_paths_2(root.left, tv)
  results.extend(total_paths_2(root.right, tv))

  for i in range(len(results)): 
    temp = root.data + results[i] 
    if temp == tv:
      total_paths_global += 1
      del results[i]  # Deleting as we don't need to count it twice
  results.append(root.value)
  return results

def total_paths_3(root: TreeNode, tv: int):
  if not root:
    return 0
  return total_paths_running_sum(root, tv, 0, {})

from typing import Dict
def total_paths_running_sum(root, tv, runningSum, pathsCount:Dict[int]):
  """
  The way that it works is that accumulates the values of the nodes in a running sum.
  If the runningSum is equals to the targetValue then we increase the path.
  So far so good. Adding the value of the node is for the case where the value of the root of the accumulated value
  that includes the root gives the target value.

  We store the runningSum in a map to count how many paths have led us to the target number.
  To find those paths, we look in the map the value of the key: runningSum - target.
  And accumulate the total paths from children nodes. Then return the total paths found

  """
  if not root:
    return 0
  
  runningSum += root.data # accumulate value
  # key to find if we already have paths that led to the target value
  sum = runningSum - tv 
  totalPaths = pathsCount.get(sum, 0)
  if runningSum == tv: # If we have a path starting from root then include it
    totalPaths += 1

  # update map with the running sum
  # increse by 1 the total of times we have seen this path
  pathsCount[runningSum] = pathsCount.get(runningSum, 0) + 1 
  # explore children
  totalPaths += total_paths_running_sum(root.left, tv, runningSum, pathsCount)
  totalPaths += total_paths_running_sum(root.right, tv, runningSum, pathsCount)
  # remove it to avoid duplicates.
  pathsCount[runningSum] = pathsCount.get(runningSum, 0) - 1 
  return totalPaths

if __name__ == "__main__":
  
  