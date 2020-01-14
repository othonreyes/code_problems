# Create a function that tells if 2 strings have one or zero edits.
# An edit can be an insertion, a replacement or a deletion of a character.
# Examples: 
# pale vs ple : True
# pales, pale: True
# pale, bale - True
# pale, pale - True
# pale, bake - False
# Output 'Mr%20John%20Smith'

### Note: Don't use extra space

import unittest
from collections import Counter

def incLessThanN(i, n):
  return 1 if i + 1 < n - 1 else 0

def oneAway(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  n = max(n1, n2)
  if n1 >= n2:
    sl = s1
    ss = s2
    nl = n1
    ns = n2
  else:
    sl = s2
    ss = s1
    nl = n2
    ns = n1

  edits = 0
  iL = 0
  iS = 0
  for _ in range(n):
    if sl[iL] != ss[iS]:
      if nl == ns:
        edits += 1
        iS += incLessThanN(iS, ns)
        iL += incLessThanN(iL, nl)
      else:
        edits += 1
        iL += incLessThanN(iL, nl)
      if edits > 1:
        return False
    else:
      iS += incLessThanN(iS, ns)
      iL += incLessThanN(iL, nl)
  # Orignial idea that didn't work
  # for _ in range(n):
  #   if sl[iL] != ss[iS]:
  #     if nl == ns: # this was right
  #       edits += 1
  #     elif iL + 1 < nl - 1 and sl[iL + 1 ] == ss[iS]: # No need to check one ahead
  #       edits += 1
  #       iL += incLessThanN(iL, nl) # this was right
  #     else: 
  #       return False
  #     if edits > 1: # this was right
  #       return False
  #     iS += incLessThanN(iS, ns) # this was right-ish, we should increment on each iteration if they are equals or not
  #     iL += incLessThanN(iL, nl)
  return True

def oneAway2(s1,s2):
  if len(s1) == len(s2):
    return one_replaced(s1, s2)
  if len(s1) == len(s2) + 1:
    return one_inserted(s1, s2)
  if len(s1) == len(s2) -1:
    return one_inserted(s2, s1)
  return False

def one_replaced(s1, s2):
  edited = False
  for c1,c2 in zip(s1,s2):
    if c1 != c2:
      if edited:
        return False
      edited = True 
  return True

def one_inserted(s1, s2):
  i = 0
  j = 0
  edited = False
  while i < len(s1) and j< len(s2):
    if s1[i] != s2[j]:
      if edited:
        return False
      edited = True
      i += 1
    else:
      i += 1
      j += 1
  return True


class Test(unittest.TestCase):
  valid = (
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'pale', True),
    ('pale', 'bake', False),
    ('apale', 'pale', True),
    ('pale', 'plaaaaaa', False)
  )

  def test(self):
    for [s1, s2, expected] in self.valid:
      print(s1,' vs ',s2)
      result = oneAway(s1, s2)
      self.assertEqual(result,expected)
    
    print('---' * 10)

    for [s1, s2, expected] in self.valid:
      print(s1,' vs ',s2)
      result = oneAway2(s1, s2)
      self.assertEqual(result,expected)

if __name__ == "__main__":
  unittest.main()