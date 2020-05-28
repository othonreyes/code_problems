"""
https://www.techiedelight.com/levenshtein-distance-edit-distance-problem/

"""

def levenshtein(x, lenx, y, leny):
  if lenx == 0:
    return leny
  if leny == 0:
    return lenx

  cost = 0 if x[lenx-1] == y[leny-1] else 1
  return min( levenshtein(x, lenx - 1, y, leny) + 1, # deletion
    levenshtein(x, lenx, y, leny - 1) + 1, # insertion
    levenshtein(x, lenx - 1, y, leny - 1) + cost
   )


def levenshtein_bu(x, lenx, y, leny):
  dp = [ [0 for _ in range(lenx + 1)] for _ in range(leny + 1)]
  
  # initialize the cost of changing every single letter for the word x
  for i in range(1, lenx  + 1):
    dp[0][i] = i
  # initialize the cost of changing every single letter for the word y
  for j in range(1, leny  + 1):
    dp[j][0] = j

  for i in range(1, lenx  + 1):
    for j in range(1, leny  + 1):
      cost = 0 if x[i-1] == y[j-1] else 1

      dp[j][i] = min(
        dp[j-1][i] + 1, # insertion
        dp[j][i - 1] + 1, # deletion
        dp[j - 1][i - 1] + cost
      )

  return dp[leny][lenx]

def levenshtein_td(x, lenx, y, leny, dp):
  if lenx == 0:
    return leny
  if leny == 0:
    return lenx
  
  if dp[leny][lenx]:
    return dp[leny][lenx]

  cost = 0 if x[lenx-1] == y[leny-1] else 1
  dp[leny][lenx] = min( levenshtein_td(x, lenx - 1, y, leny, dp) + 1, # deletion
    levenshtein_td(x, lenx, y, leny - 1, dp) + 1, # insertion
    levenshtein_td(x, lenx - 1, y, leny - 1, dp) + cost
   )
  return dp[leny][lenx]

if __name__ == "__main__":
  x = "kitten"
  y = "sitting"
  print(levenshtein(x, len(x), y, len(y)))
  print(levenshtein_bu(x, len(x), y, len(y)))

  dp = [ [None for _ in range(len(x) + 1)] for _ in range(len(y) + 1)]
  print(levenshtein_td(x, len(x), y, len(y), dp))