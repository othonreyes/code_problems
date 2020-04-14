# Create a function that implements a basic compression algorithm by counting the chars
# thtat are present in a string, if the result string is longer than input
# then return original input.
# 
# Examples: 
# aaabcccccaaa: a3b1c5a3
# abcdef: abcdef
# aaaaaaaaaaba: a10b1a1

### Note: Don't use extra space

import unittest
from collections import Counter

def compress2(s1):
  newStr = []
  count = 0
  for i in range(len(s1)):
    # Explanation
    # the i != 0 is used to deal with the first character.
    # we could have done but requirs extra code:
    # char = s1[0] # requires  to check if the s1 is not empty
    # - or -
    # char = '' # requires to check if char != ''
    if i != 0 and s1[i] != s1[i-1]: 
      newStr.append(s1[i-1] + str(count)) 
      count = 0
    count += 1
  newStr.append(s1[-1] + str(count)) # we do this to deal with the last characters
  return min(s1, ''.join(newStr), key=len)

def compress(s1):
  newStr = ''
  char = ''
  count = 0
  for i in range(len(s1)):
    if char != s1[i]:
      if char != '': # we do this to deal with the initial case
        newStr += char + str(count)
      char = s1[i]
      count = 1
    else:
      count += 1
  newStr += char + str(count) # we do this to deal with the last characters
  if len(newStr) > len(s1):
    return s1
  return newStr

class Test(unittest.TestCase):
  valid = (
    ('aaabcccccaaa', 'a3b1c5a3'),
    ('abcdef', 'abcdef'),
    ('aaaaaaaaaaba', 'a10b1a1')
  )

  def test(self):
    for [input, expected] in self.valid:
      print(input,' vs ',expected)
      result = compress(input)
      self.assertEqual(result, expected)
    
    

if __name__ == "__main__":
  unittest.main()