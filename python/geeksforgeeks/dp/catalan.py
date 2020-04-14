

def catalan_rec(n):
  if n <= 1:
    return 1
  res = 0
  for i in range(n): 
    res += catalan_rec(i) * catalan_rec(n-i-1)
  return res

def catalan_rec_td(n, arr):
  if n <= 1:
    return 1
  if arr[n] > 0:
    return arr[n]
  res = 0
  for i in range(n):  
    res += catalan_rec_td(i, arr) * catalan_rec_td(n-i-1, arr)
  arr[n] = res
  return res

def catalan_rec_bu(n):
  catalan = [0] * (n+1)
  catalan[0] = 1
  catalan[1] = 1
  for i in range(2, n + 1):
    catalan[i] = 0
    for j in range(i):
      catalan[i] = catalan[i] + catalan[j] + catalan[i-j-1]

  return catalan[n]


if __name__ == "__main__":
  for i in range(10):
    catalan_rec(i)
  
  for i in range(10):
    arr = [0] * i 
    catalan_rec(i, arr)
    
