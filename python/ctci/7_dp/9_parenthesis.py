def parenthesis(n):
  r = set()
  arr = [None] * (n * 2)
  paren(0,n,n,arr, r)
  return r

## Weaving or bracktracking, you are with 2 groups of items so first you 
# recursively call one progressing in the first group of elements and then call
#  the other one recrusively too progressing on the other gorup of elements.
# you also need a condition to not fall into a invalid state
def paren(ix,left,right,arr, r):
  if left < 0 or right < left :
    return
  if left == 0 and right == 0:
    r.add("".join(arr))
    return
  if left > 0:
    arr[ix] = '('
    paren(ix+1, left - 1, right, arr, r)  
  if right > 0:
    arr[ix] = ')'
    paren(ix+1, left, right - 1, arr, r)

if __name__ == "__main__":
  print(parenthesis(1))
  print(parenthesis(2))
  print(parenthesis(3))