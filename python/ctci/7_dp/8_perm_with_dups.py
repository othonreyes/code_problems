from collections import Counter


def permutations(input):
  chars = Counter(input)
  result = set()
  perms("", chars, result, len(input))
  return result

def perms(prefix, chars, result, n):
  if len(prefix) == n:
    result.add(prefix)
    return

  for k,v in chars.items():    
    if v > 0:      
      chars[k] = v - 1
      perms(prefix + k, chars, result, n)
      # Doing backtracking
      chars[k] = v



if __name__ == "__main__":                                                                                                                          
  print(permutations('aa'))
  print(permutations('abb'))