"""
https://www.geeksforgeeks.org/gold-mine-problem/

Gold Mine Problem


Input : mat[][] = [[ 1, 3, 3],
                    2, 1, 4],
                    0, 6, 4]];
Output : 12 
  (1,0)->(2,1)->(2,2)]

Input: mat[][] =  [[  1, 3, 1, 5],
                    [2, 2, 4, 1],
                    [5, 0, 2, 3],
                    [0, 6, 1, 2]];
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] =   [ [10, 33, 13, 15],
                    [22, 21, 04, 1],
                    [5, 0, 2, 3],
                    [0, 6, 14, 2]];
Output : 83
"""

def max_gold(mine):
  # find the starting point in the column
  n = len(mine)
  m = len(mine[0])
  gold = [[0 for _ in range(m + 1)] for _ in range(n + 2)]

  profit = 0
  
  for j in reversed(range(m)):
    for i in reversed(range(n)):
      offset_r = i + 1
      gold[offset_r][j] = mine[i][j] + max(
        gold[offset_r + 1][j + 1],
        gold[offset_r][j + 1],
        gold[offset_r - 1][j + 1])
      profit = max(profit, gold[offset_r][j])

  for i in range(len(gold)):
    print(gold[i])
  return profit

if __name__ == "__main__":
  mine = [[1, 3, 3],
          [2, 1, 4],
          [0, 6, 4]]
  print(max_gold(mine))

  mine = [[  1, 3, 1, 5],
          [2, 2, 4, 1],
          [5, 0, 2, 3],
          [0, 6, 1, 2]]
  print(max_gold(mine))
  