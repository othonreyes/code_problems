# Write a function that rotates a martix of N by N
import unittest
from collections import Counter


def rotate(m):
  n = len(m[0])
  start = 0
  end = n
  while start < end:
    for i in range(end-start-1):
      temp=m[start][start + i]
      m[start][start + i] = m[end-1-i][start]
      m[end-1-i][start] = m[end-1][end - 1 - i]
      m[end-1][end - 1 - i] = m[start + i][end - 1]
      m[start + i][end - 1] = temp
    start += 1 
    end -= 1 
  return m

class Test(unittest.TestCase):
  valid = (
    ([[1,2],
      [3,4]], [[3,1],
              [4,2]]),
    ([[1,2,3],
      [4,5,6],
      [7,8,9]], [[7,4,1],
                [8,5,2],
                [9,6,3]]),
    ([[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]], [ [13,9, 5,1],
                        [14,10,6,2],
                        [15,11,7,3],
                        [16,12,8,4]])
  )

  def test(self):
    for [input, expected] in self.valid:
      print(input,' vs ',expected)
      result = rotate(input)
      self.assertEqual(result, expected)
    
    

if __name__ == "__main__":
  unittest.main()