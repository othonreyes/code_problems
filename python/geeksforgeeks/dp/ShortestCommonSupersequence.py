"""
Shortest Common Supersequence

https://www.techiedelight.com/shortest-common-supersequence-introduction-scs-length/

The shortest common supersequence (SCS) is the problem of finding the shortest supersequence Z of given sequences X and Y such that both X & Y are subsequences of Z.
"""

def scs(A,B,m,n):
  if n==0 or m == 0:
    return n + m
  if A[m-1] == B[n -1]:
    return scs(A,B,m-1, n-1) + 1
  else:
    return min(scs(A,B,m-1, n) + 1, scs(A,B,m, n - 1) + 1)

def scs_td(A,B,m,n, map):
  if n==0 or m == 0:
    return n + m
  key = A[:m-1] + "|" + B[:n-1]
  if key in map:
    return map[key]  
  if A[m-1] == B[n -1]:
    map[key] = scs_td(A,B,m-1, n-1, map) + 1
  else:
    map[key] = min(scs_td(A,B,m-1, n, map) + 1, scs_td(A,B,m, n - 1, map) + 1)
  return map[key]

def scs_bu(A,B,m,n):
  dp = [ [0 for _ in range(n+1)] for _ in range(m+1)]
  # initiazlie with the value of i becasue it's like saying that the
  # this is the size of the superset at the ith point
  for i in range(m+1):
    dp[i][0] = i 
  for j in range(n+1):
    dp[0][j] = j

  for i in range(1,m+1):
    for j in range(1,n+1):
      if A[i-1] == B[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

  return dp[m][n]

if __name__ == "__main__":
  X ="ABCBDAB" 
  Y ="BDCABA"
  print(scs(X,Y, len(X), len(Y)))
  print(scs_td(X,Y, len(X), len(Y),dict()))
  print(scs_bu(X,Y, len(X), len(Y)))
