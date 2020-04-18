def queens(board):
  """
  Doesn't work because the solution is not recursive. It constraints to only
  checking the possible solutions of plaicng the queen in a given spot.

  Another thing, no need to store the whole board, it's just enough to have a
  one dimensional array of the columns.
  One more thing, the diagonal cna be calculated byt the distance between rows 
  and columns. when r1 - r2 == c1 - c2 then they are in a diagonal.

  How to fix it?
  Regardless of how to validate that is valid, what we needed to check, recursively, 
  if there was a solution from the starting point. And if not, try the next 
  possible solution. We tried that artificially by storing the last result but
  that was a hacky solution.
  """
  r = len(board)
  c = len(board[0])
  i = 0
  j = 0
  x,y=-1,-1
  while i < r:
    while j < c:
      # skip first space found
      if board[i][j] == 0:
        if x  == -1 and canPlaceQueen(board, i,j, r, c):
          y = i
          x = j
          continue
        else:
          if canPlaceQueen(board, i,j, r, c):
            board[i][j] = 1
          else:
            board[y][x] = 1
      j+=1
    i+=1

def canPlaceQueen(board, i,j, r, c):
  # if i < 0 or j < 0 or i == r or j ==c:
  #   return True
  if isVerticalFree(board, j, r, c) and \
    isHorizontalFree(board, i, r, c) and \
    isDiagonalFree(board, i,j, r, c):
    return True
  return False
  
def isVerticalFree(board, j, r, c):
  for i in range(r):
    if board[i][j] != 0:
      return False
  return True

def isHorizontalFree(board, i, r, c):
  for j in range(c):
    if board[i][j] != 0:
      return False
  return True

def isDiagonalFree(board, i, j, r, c):
  # find the begining of the diagonal
  y = i
  x = j
  while y >= 0 and x >= 0:
    y -= 1
    x -= 1
  while y < r and x < c:    
    if board[y][x] != 0:
      return False
    x += 1
    y += 1

  y = i
  x = j
  while y >= 0 and x < c:
    y -= 1
    x += 1
  while y < r and x >=0:
    if board[y][x] != 0:
      return False
    y += 1
    x -= 1

  return True


def queues_book_solution(row, columns, result):
  """
  columns - onedimanesional array. each position represents the row, the value represents the column
  """
  
  if row == len(columns):    
    result.append(columns.copy())
    return
  # we want to iterate over all the possible columns
  for col in range(len(columns)):
    # at first, i thought that we needed a flag to detect if we couldn't find a solution after iterating 
    # all the columsn. but then realized that if we don't find it, then the base condition would never be
    # called. that's why we don't need it.
    if canPlace(columns, row, col):
      columns[row] = col
      queues_book_solution(row + 1, columns, result)

def canPlace(columns, row, col):
  # We only need to check all rows from 0 to row and not the 8 rows becasue we have
  # only placed a value all the way until row.  
  for row2 in range(row):
    col2 = columns[row2]
    if col2 == col:
      return False
    
    # we need the absolute value because we don't know which column is bigger
    col_distance = abs(col - col2)
    row_distance = row - row2
    if col_distance == row_distance:
      return False
  return True

if __name__ == "__main__":
  # board = [[0 for _ in range(8)] for _ in range(8)]
  # queens(board)
  # for i in 8:
  #   print(board[i])

  results = []
  columns = [0] * 8
  queues_book_solution(0, columns, results)
  for i in range(len(results)):
    r = results[i]
    print(r)
    # for j in range(len(r)):
    #   print(r[j])