def permutation(text, anchor, p):
  if anchor == len(text):
    p.add("".join(text))
    return
  for i in range(anchor, len(text)):
    text[anchor], text[i] = text[i], text[anchor]
    permutation(text, anchor + 1, p)
    text[anchor], text[i] = text[i], text[anchor]


if __name__ == "__main__":
  text = "abc"
  p = set()
  permutation(list(text), 0, p)
  print(p)

  text = "abcd"
  p = set()
  permutation(list(text), 0, p)
  print(p)