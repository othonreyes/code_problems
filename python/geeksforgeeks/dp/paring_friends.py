"""
https://www.geeksforgeeks.org/friends-pairing-problem/
Input  : n = 3
Output : 4

Explanation
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.
"""
from typing import List
#### Doesn't work
def pair_friends(n:int) -> int:
  if (n == 0):
    return 0
  return len(pair(n))

def pair(n: int) -> List[List[List[int]]]:
  if (n == 1):
    return [[[1]]]
  result = []
  prev = pair(n-1)
  #inter = prev.copy() if len(prev) == 1 else prev[0].copy()
  inter = prev[0].copy()
  inter.append([n])
  result.append(inter)
  for i in range(len(prev)):
    current = prev[i]
    for j in range(len(current)):
      copy = current[j]
      copy.append(n)
      current[j] = copy
      
      result.append([current])

      copy.pop() # backtrack
      current[j] = copy
  return result


if __name__ == "__main__":
  n = 3
  result = pair_friends(n)
  print("{}".format(result))

  print("{}".format(pair_friends(4)))