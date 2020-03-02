"""
https://www.geeksforgeeks.org/count-the-number-of-words-with-given-prefix-using-trie/

Given a list of string str[] and a prefix string pre. The task is to count the number of words in list of string with given prefix using trie.

Input: str = [ “apk”, “app”, “apple”, “arp”, “array” ], pre = “ap”
Output: 3
"""

class Node:
  def __init__(self, word:bool = False):
    self.children = [None] * 26
    self.word = word

def insert(root, word:str) -> Node:
  n = root
  for i in word:
    position = ord(i) - ord('a')
    if n.children[position]:
      n = n.children[position]
    else:
      n.children[position] = Node()
      n = n.children[position]
  n.word = True

def search(root, word) -> bool:
  n = root
  for n in word:
    position = ord(n)
    if n.children[position]:
      n = n.children[position]
    else:
      return False
  return n is not None

def print_trie(root: Node, s = ''):
  if root.word:
    print(s)
  for i in range(len(root.children)):
    if root.children[i]:
      print_trie(root.children[i], s+chr(i+ord('a')))

def count_words_prefix(root: Node, prefix:str) -> int:
  n = root
  # find the prefix doing a DFS
  for i in prefix:
    pos = ord(i) - ord('a')
    if n.children[pos]:
      n = n.children[pos]
    else:
      return 0

  # starting from the pointer node, do a DFS to find all words with that prefix
  count = 0
  children = [n]
  while children:
    n = children.pop(0)
    if n.word:
      count += 1
    for i in range(len(n.children)):
      if n.children[i]:
        children.append(n.children[i])

  return count


if __name__ == "__main__":
  root = Node()
  insert(root, "app")
  print_trie(root)
  print('---'*10)

  # inserting more words
  insert(root, "apk")
  insert(root, "apple")
  insert(root, "apple")
  insert(root, "arp")
  insert(root, "array")
  print_trie(root)
  print(count_words_prefix(root, "ap"))