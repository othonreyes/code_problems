"""
Notes:
- it's easir to think about this problem from the top-down perspective as 
  thinking from the "n" step makes you consider the possible combinations of hops
  as compared to the bottoms up approach. in the bottoms up approach, you start 
  with step 1 and immediatly rulled out the other hops
- The problem doesn't ask for the unique combinations of steps but all possible
  combinations, even repeated ones.
"""
def hops(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return hops(n-1) + hops(n-2) + hops(n-3) 

def hops_td(n):
  m = [-1] * (n + 1)  
  return hops_m(n, m) 

def hops_m(n, m):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if m[n] != -1: 
    return m[n]
  m[n] = hops_m(n - 1, m) + hops_m(n - 2, m) + hops_m(n - 3, m)
  return m[n]

def hops_bu(n):
  m = [-1] * (n + 1)
  m[0] = 1 # assign base case

  for i in range(1, n + 1):
    # replaces the recursive calls
    h1 = m[i - 1] if i - 1 >=0 else 0
    h2 = m[i - 2] if i - 2 >=0 else 0
    h3 = m[i - 3] if i - 3 >=0 else 0
    m[i] = h1 + h2 + h3
  return m[n]


if __name__ == "__main__":
  n = 4
  print(hops(n))
  print(hops_td(n))
  print(hops_bu(n))