"""
https://www.geeksforgeeks.org/gold-mine-problem/
Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(2,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
"""

from typing import List

def gold_mine(input:List[List[int]]) -> int:
  result = 0
  cols = len(input[0])
  rows = len(input)
  for j in reversed(range(cols)):
    for i in reversed(range(rows)):
      input[i][j] = input[i][j] + \
        max(
          input[i-1][j+1] if i - 1 >= 0 and j + 1 < cols else 0, \
          input[i][j+1] if j + 1<rows else 0, \
          input[i+1][j+1] if i + 1 < rows and j + 1 < cols else 0
          )
      result = max(input[i][j], result)
  return result

if __name__ == "__main__":
  input = [[1, 3, 3],
          [2, 1, 4],
          [0, 6, 4]]
  result = gold_mine(input)
  print("Result {}".format(result))
