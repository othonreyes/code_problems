"""
Trie implementation:
- search
- insert
"""
class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.__root = TrieNode()
  
  def insert(self, word):    
    traveler = self.__root
    for i in word:
      index = ord(i) - ord('a')
      if not traveler.children[index]:
        traveler.children[index] = TrieNode()
      traveler = traveler.children[index]
    traveler.endOfWord = True

  def search(self, word):
    traveler = self.__root
    for i in word:
      index = ord(i) - ord('a')
      if not traveler.children[index]:
        return False
      traveler = traveler.children[index]
    return True, traveler.endOfWord
      

if __name__ == "__main__":
  trie = Trie()
  trie.insert('there')
  trie.insert('their')
  trie.insert('the')
  print(trie.search('the'))
  print(trie.search('there'))
  print(trie.search('ther'))