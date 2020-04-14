from typing import List

class Solution:
  def explore_cell(self, grid, i, j, r, c):
    """
    returns 
        0 - empty
        2 - already rotten
        4 - to get rotten
        3 - unreachable
    """
    if grid[i][j] == 2 or grid[i][j] == 0:
        return grid[i][j]
    
    empty_cells = True
    if (i - 1 >= 0 and grid[i-1][j] != 0) or \
        (i + 1 < r and grid[i+1][j] != 0) or \
        (j - 1 >= 0 and grid[i][j-1] != 0) or \
        (j + 1 < c and grid[i][j+1] != 0) : 
        empty_cells = False
    return 3 if empty_cells else grid[i][j]
      
  def rott_oranges(self, grid, r, c, x, y, minutes):
    if x >= 0 and x < r and y >= 0 and y < c :
        if grid[x][y] == 0:
            return minutes -1
        # if grid[x][y] == 2:
        #     return minutes -1
        if grid[x][y] == 1:
            grid[x][y] = 2
    else:
        return minutes - 1
    return max(
        self.rott_oranges(grid, r, c, x - 1, y, minutes + 1),
        self.rott_oranges(grid, r, c, x + 1, y, minutes + 1),
        self.rott_oranges(grid, r, c, x, y - 1, minutes + 1),
        self.rott_oranges(grid, r, c, x, y + 1, minutes + 1)
    )
  
  def orangesRotting(self, grid: List[List[int]]) -> int:        
    oranges = 0
    rotten = 0
    x = -1
    y = -1        
    r = len (grid)
    c = len (grid[0])
    for i in range(r):            
        for j in range(c):
            result = self.explore_cell(grid, i, j, r, c)
            if result == 3:
                return -1
            if result == 2 :
                if x == -1:
                    x = i
                    y = j
                rotten += 1
            if result > 0 :
                oranges += 1 
    if oranges == rotten:
        return 0
      
    return self.rott_oranges(grid, r, c, x, y, 0)

if __name__ == "__main__":
  grid = [[2,1,1],[1,1,0],[0,1,1]]
  s = Solution()
  s.orangesRotting(grid)