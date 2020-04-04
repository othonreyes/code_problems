def robot_grid_rec(grid, n, m, mem):
  if n < 0 :
    return 999
  if m < 0 :
    return 999
  if mem[n][m] != 999:
    return mem[n][m]
  if grid[n][m] == 999:
    return 999
  if n == 0 and m == 0:
    mem[n][m] = 0
    return 0
  top = robot_grid_rec(grid, n - 1, m, mem)
  left = robot_grid_rec(grid, n, m-1, mem)
  if top == 999 and left == 999:
    raise AssertionError("Cant find a solution")
  mem[n][m] = min(top, left) + 1
  return mem[n][m]


def robot_grid_td(grid):
  n = len(grid)
  m = len(grid[0])
  mem = [[999 for _ in range(m + 1)] for _ in range(n + 1)]
  mem[0][1] = -1 # BASE CASE THAT IS THE ROBOT STARTING POSITION
  mem[1][0] = -1
  for i in range(1, n+1):
    for j in range(1, m+1):
      if grid[i][j] == 999:
        continue
      top = mem[i-1][j]
      left = mem[i][j-1]
      if top == 999 and left == 999:
        raise AssertionError("Cant find a solution")
      mem[i][j] = min(top, left) + 1


def printPath(mem, n, m):
  print("(0,0)")
  i = 0
  j = 0
  while i != n -1 or j != m - 1:
    # check right
    right = mem[i][j + 1] if j + 1 < m else 999
    down = mem[i + 1][j] if i + 1 < n else 999
    if right < down:      
      print("({},{})".format(i, j + 1))
      j += 1
    else: 
      print("({},{})".format(i + 1, j))
      i += 1

def print_mem(mem):
  for i in range(len(mem)):
    print(mem[i])
  

if __name__ == "__main__":
  grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]
  n = len(grid)
  m = len(grid[0])
  mem = [[999 for _ in range(m)] for _ in range(n)]
  robot_grid_rec(grid, n-1, m-1, mem)
  print_mem(mem)
  printPath(mem, n, m)

  grid = [
    [0,-1,0],
    [0,-1,0],
    [0,0,0]
  ]

  grid = [
    [0,-1,0],
    [0,-1,0],
    [0,-1,0]
  ]