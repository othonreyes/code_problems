# Write a function to see if a string is a permutation of palindrom.
#Input: 'Tact coa' 
#Retuls trues i.e possible palindromes 'taco cat' ,'atco cta' 
# -----------------------------------------------------------
# Solution:
# Count the chars and ignore whatever is not a char.
# Then iterate over again and check that there are only 1 char with a odd number
# T: O(n)

import unittest
from collections import Counter

def from_palindrome(input):
  chars = Counter()
  # count the characters
  for i in input:
    if not('a' <= i and i <= 'z'):
      continue
    chars[i] += 1

  odd_char_count = 0
  for key in chars:
    if chars[key] % 2 != 0:
      odd_char_count += 1
  return odd_char_count <= 1 

class Test(unittest.TestCase):
  valid = (
    'Tact coa'    
  )

  def test(self):
    for i in self.valid:
      self.assertTrue(from_palindrome(i))

if __name__ == "__main__":
  unittest.main()