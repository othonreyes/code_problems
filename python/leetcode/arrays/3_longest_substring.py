# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = dict()
        i = 0
        longest = 0

        n = len(s)
        j = 0
        while i < n and j < n:
          if memory.get(s[j]):
            del memory[s[i]]
            i += 1
          else:         
            memory[s[j]] = 1
            j += 1
            longest = max(longest, j-i)

        # memory = dict()
        # for j in range(len(s)):
        #   if memory.get(s[j]) or memory.get(s[j]) == 0:          
        #     i = max(memory.get(s[j]), i) + 1
        #   memory[s[j]] = j + 1
        #   longest = max(longest, j-i+1) 
        
        return longest


class MyTest(unittest.TestCase):
  valid = (
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('aab', 2),
    (' ', 1),
    ('dvdf', 3),
    ('tmmzuxt', 5)
  )

  def test(self):
    solution = Solution()
    for [s, n] in self.valid:
      print(s)
      self.assertEqual(n, solution.lengthOfLongestSubstring(s))

if __name__ == "__main__":
  unittest.main()