# Create a method that replaces ' ' with '%20
# Input: 'Mr John Smith      ', 13
# Output 'Mr%20John%20Smith'

### Note: Don't use extra space
### Tips: counting spaces is used to find the index to start.
#### It is easier to transform a string starting from the end as we don't overwrite useful data.

import unittest
from collections import Counter

def urlify(arr, length):
  spaces = 0
  for i in range(length):
    if arr[i] == ' ':
      spaces +=1
  
  index = length + spaces * 2
  print(index)
  for i in reversed(range(length)):
    if arr[i] == ' ':
      arr[index - 1] = '0'
      arr[index - 2] = '2'
      arr[index - 3] = '%'
      index -= 3
    else:
      arr[index - 1] = arr[i]
      index -= 1
    
  str = ''.join(arr)
  print('Result: ', str)
  return str

class Test(unittest.TestCase):
  valid = (
    ['Mr John Smith    ', 13, 'Mr%20John%20Smith']
  )

  def test(self):
    #for [input, size, expected] in self.valid:
      #result = urlify(i[0], i[1])
      result = urlify(list(self.valid[0]), self.valid[1])
      self.assertEqual(result, self.valid[2], "The strings should match")

if __name__ == "__main__":
  unittest.main()