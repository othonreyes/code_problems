# Given 2 strings, write a program to find is one is a permutation of another

def is_permutation(input, permutation):
  if not (len(input) == len(permutation)):
    return False
  chars = {}
  for i in input:
    if chars.get(i) is None:
      chars[i] = 1
    else:
      chars[i] = 1 + chars[i]
  
  for i in permutation:
    if chars.get(i) is None:
      return False #We found a character that doesn't exist in the first string
    else:
      chars[i] = chars[i] - 1
      if chars[i] == 0:
        del chars[i]
  if len(chars)>0:
    return False  
  return True

# Test scnearios:
# 1. unique chars
# 1. repeated chars
# 1. different lengths
# 1. first string has more one char than second string
# 1. second string has more one char than first string

input = 'a'
permutation = 'a'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = 'a'
permutation = 'b'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = 'ab'
permutation = 'ba'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = 'aaaaaab'
permutation = 'aaabaaa'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = '1'
permutation = 'aaabaaa'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = 'banana'
permutation = 'nabana'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))

input = 'abcde'
permutation = 'abcdf'
print('Is ', permutation, ' a permutation of ', input, '? ', is_permutation(input, permutation))
