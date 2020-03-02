# https://www.geeksforgeeks.org/given-an-absolute-sorted-array-and-a-number-k-find-the-pair-whose-sum-is-k/
"""
Given an absolute sorted array and a number K, find the pair whose sum is K
Given an absolute sorted array arr[] and a number K, the task is to find a pair of elements in the given array that sum to K. An absolute sorted array is an array of numbers in which |arr[i]| ≤ |arr[j]| whenever i < j.

Examples:

Input: arr[] = {-49, 75, 103, -147, 164, -197, -238, 314, 348, -422}, K = 167
Output: 3 7
(arr[3] + arr[7]) = (-147 + 314) = 167.



Input: arr[] = {-8, 10, -15, 12, 24}, K = 22
Output: 1 3

"""
import logging 
import unittest

log = logging.getLogger('Console')
log.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(consoleHandler)

def find_pair(items:[int], k:int)->[int]:
  """
  T: O(n)
  S: O(n)
  """
  seen = dict()
  pair = []
  for i in range(len(items)):
    value = items[i]
    delta = k - value
    if seen.get(str(delta)):
      return [seen.get(str(delta)), i]
    else:
      seen[str(items[i])] = i
  return []

# Would work if the array were a sorted array not a absolute sorted array
def find_pair_two_pointer(items:[int], k:int)->[int]:
  n = len(items)
  i, j = 0, n-1  
  while i < n and j >= 0:
    d = items[i] + items[j]
    if d == k:
      return [i, j]
    elif d > k:
      j -= 1
    elif d < k:
      i += 1
  return []

class Test(unittest.TestCase):
  valid = (
    ( [-49, 75, 103, -147, 164, -197, -238, 314, 348, 422], 167, [3,7]),
    ([-8, 10, -15, 12, 24], 22,[1,3])
  )

  def test(self):
    for k in self.valid:
      result = find_pair(k[0], k[1])
      self.assertEqual(k[2], result)
      # result = find_pair_two_pointer(k[0], k[1])
      # self.assertEqual(k[2], result)


if __name__ == "__main__":
  unittest.main()