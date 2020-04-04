"""
https://www.geeksforgeeks.org/min-cost-path-dp-6/
For example, in the following figure, what is the minimum cost path to (2, 2)?
[1,2,3]
[4,8,2]
[1,5,3]

The path with minimum cost is highlighted in the following figure. The path is (0, 0) –> (0, 1) –> (1, 2) –> (2, 2). The cost of the path is 8 (1 + 2 + 2 + 3).

"""

def min_cost_path(matrix, sp, tp):
  r = len(matrix)
  c = len(matrix[0])
  pc = [[0 for _ in range(c)] for _ in range(r)]
  return mcp(matrix, sp, tp, r, c, pc)

def mcp(matrix, sp, tp, r, c, pc):
  if tp[0] < 0 or tp[0] > r or \
    tp[1] < 0 or tp[1] > c:
    return 999999

  if pc[tp[0]][tp[1]] > 0:
    return pc[tp[0]][tp[1]]

  if sp[0] == tp[0] and sp[1] == tp[1]:
    pc[tp[0]][tp[1]] = matrix[tp[0]][tp[1]]
    return matrix[tp[0]][tp[1]]

  # Diagonals are allowed so we move up, diagonal or left
  pc[tp[0]][tp[1]] = matrix[tp[0]][tp[1]] + min(
    mcp(matrix, sp, (tp[0]-1, tp[1]), r, c, pc), # up
    mcp(matrix, sp, (tp[0]-1, tp[1]-1), r, c, pc), # diagonal
    mcp(matrix, sp, (tp[0], tp[1]-1), r, c, pc) # left
   )
  return pc[tp[0]][tp[1]]

def mcp_bottmon_up(matrix, sp, tp):
  r = len(matrix)
  c = len(matrix[0])
  pc = [[0 for _ in range(c + 1)] for _ in range(r + 1)]  
 
  for i in range(r + 1):
    pc[i][0] = 999
  for j in range(c + 1):
    pc[0][j] = 999
 
  for i in range(r):
    for j in range(c):
      min_val = min( 
        pc[i+1][j], # up 
        pc[i][j], # diagonal
        pc[i][j+1] # right
        )
      min_val = 0 if min_val == 999 else min_val
      pc[i+1][j+1] = matrix[i][j] + min_val
  return pc[i+1][j+1]

  # Diagonals are allowed so we move up, diagonal or left
  pc[tp[0]][tp[1]] = matrix[tp[0]][tp[1]] + min(
    mcp(matrix, sp, (tp[0]-1, tp[1]), r, c, pc), # up
    mcp(matrix, sp, (tp[0]-1, tp[1]-1), r, c, pc), # diagonal
    mcp(matrix, sp, (tp[0], tp[1]-1), r, c, pc) # left
   )
  return pc[tp[0]][tp[1]]

if __name__ == "__main__":
  matrix = [[1,2,3],
            [4,8,2],
            [1,5,3]]
  print(min_cost_path(matrix, (0,0), (2,2)))
  print(mcp_bottmon_up(matrix, (0,0), (2,2)))
  