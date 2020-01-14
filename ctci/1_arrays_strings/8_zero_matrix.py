# Create a function that finds the zeros in a matrix of MxN and sets to 0 the row and the column 
# where the element was found

import unittest
from collections import Counter

def zero_matrix(m):
  rows_len = len(m)
  cols_len = len(m[0])
  rows = []
  cols = []
  # find the zeros first
  for i in range(rows_len):
    for j in range(cols_len):
      if m[i][j] == 0:
        rows.append(i)
        cols.append(j)
  
  for r in rows:
    # Nullify the row
    for j in range(cols_len):
      m[r][j] = 0
  
  for c in cols:
    # Nullify the row
    for i in range(rows_len):
      m[i][c] = 0

  return m

class Test(unittest.TestCase):
  valid = (
    ([[0,2],
      [3,4]], [[0,0],
              [0,4]]),
    ([[0,2,3],
      [4,5,6],
      [7,8,0]], [[0,0,0],
                [0,5,0],
                [0,0,0]]),
    ([[1,2,0,4],
      [5,6,7,8],
      [9,0,11,12],
      [13,14,15,16]], [ [0, 0,0,0],
                        [5, 0,0,8],
                        [0, 0,0,0],
                        [13,0,0,16]])
  )

  def test(self):
    for [input, expected] in self.valid:
      print(input,' vs ',expected)
      result = zero_matrix(input)
      self.assertEqual(result, expected)
    
  
if __name__ == "__main__":
  unittest.main()