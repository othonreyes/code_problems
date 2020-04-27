from math import sqrt
def jumpSearch(a):
  n = len(a)
  m = int(sqrt(n))
  i = 0
  while a[i] is None and i < n:
    i += m
  # find first 
  for j in reversed(range(n)):
    if a[j]:
      return j
  return 0
def merge(a, b):
    # find last position of A
    i = jumpSearch(a)
    end = len(a) - 1
    j = len(b) - 1
    while i>=0 and j>=0:
      if(a[i]>b[j]):
        a[end] = a[i]
        i-=1
      else:
        a[end] = b[j]
        j-=1
      end -= 1

  
if __name__ == "__main__":
  A = [1,2,4,5,6, None, None,None]
  B = [2,4,9]
  merge(A,B)
  print(A)
    