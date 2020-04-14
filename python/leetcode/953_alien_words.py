from typing import List

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    # find the largest word
    larges_index = -1
    largest = 0
    n = len(words)
    for i in range(n):
        if largest < len(words[i]):
            largest = len(words[i])
            largest_i = i
    
    # Then check the words        
    for i in range(len(words[largest_i])):
      minindex = None
      for j in range(n):
        if minindex == None:
          if i < len(words[j]):
            minindex = order.index(words[j][i])
            continue
          else: 
            minindex = -1
        word_index = -1
        if i < len(words[j]):
          word_index = order.index(words[j][i])
        if minindex > word_index:
          return False
              
    return True 

if __name__ == "__main__":
  s = Solution()
  print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
