# implement an algorith to determine if a string has all unique characters. what if you can't use an additional structure?

def is_unique(input):
  base  = 64
  visited = 0
  for i in input:
    pos = ord(i) - ord('A')
    if visited & (1<<pos) :
      return False
    visited |= (1 << pos)
  return True

input = 'abcdea'.upper()
print('is ', input, ' unique?', is_unique(input))
input = 'whisper'.upper()
print('is ', input, ' unique?', is_unique(input))