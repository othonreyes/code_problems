# Write a function that checks that s2 is string roration of s1 but you can call isSubstring once

import unittest
from collections import Counter

def isRotation(s1, s2):
  s3 = s2 + s2
  return s1 in (s2 + s2)

def isRotation2(s1, s2):
  n = len(s1)
  diff = n//2
  subs1 = s1[-1 * diff]
  
  # find where the word ends
  # TODO: rethink the algorithm based on the rotation
  j = 0
  found = -1
  for i in range(len(s2)):
    # TODO: checks for consecutives
    if s2[i] == subs1[j]:
      if i-1>=0 and diff == 1:
        continue
      found = i
      j += 1
      if j == diff:
        break;
    else:
      j = 0
      found = -1
  
  s3 = s2[found:] + s2[0:found-1]
  return s1 in s3

class Test(unittest.TestCase):
  valid = (
    ("watterbottle", "tlewatterbot",True),
    ("watterbottle", "watterbottle",True),
    ("is", "si", True),
    ("has", "ash", True),
    ("has", "sha", True),
    ("ass", "sas", True),
    ("ass", "ssa", True)
  )

  def test(self):
    for [s1, s2, expected] in self.valid:
      print(s1,' vs ', s2)
      result = isRotation(s1,s2)
      self.assertEqual(result, expected)
    print(' --- ' * 5)
    for [s1, s2, expected] in self.valid:
      print(s1,' vs ', s2)
      result = isRotation2(s1,s2)
      self.assertEqual(result, expected)
    
  
if __name__ == "__main__":
  unittest.main()