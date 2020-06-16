"""
https://www.techiedelight.com/partition-problem/

Very similar to the coin problem
"""

def cut_rod(length, prices, rod, ix): 
  """
  Solution that is more linear but harder to understand
  """
  if rod <= 0 or ix < 0:
    return 0
  # find index of available price for the length of the rod  
  leng = length[ix]
  priceIx = prices[ix]
  nextIx = min(ix, rod - leng - 1)
  include = priceIx + cut_rod(length, prices, rod - leng, nextIx)
  exclude = cut_rod(length, prices, rod, ix - 1)
  return max(include, exclude)

def cut_rod2(prices, rod): 
  if rod <= 0:
    return 0
  maxProfit = 0
  for i in range(rod):
    profit = prices[i] + cut_rod2(prices, rod - (i+1))
    maxProfit = max(maxProfit, profit)

  return maxProfit

def cut_rod_td(prices, rod, mem):
  if rod <= 0:
    return 0
  if mem[rod] is not None:
    mem[rod]
  maxProfit = 0
  for i in range(rod):
    profit = prices[i] + cut_rod2(prices, rod - (i+1))
    maxProfit = max(maxProfit, profit)
  mem[rod] = maxProfit
  return mem[rod]

# def cut_rod_bu(prices, rod):
#   dp = [[0 for _ in range(len(prices) + 1)] for _ in range(rod+1)]

#   for i in range(1,rod + 1):
#     dp[0][i] = prices[i]
  
#   for i in range(1, rod+1):
#     for j in range(1, i + 1): # the list of prices can't exceed the length of the rod
#       dp[i][j] = max(dp[i-1][j-1], prices[j-1] + dp[i-j][j])
#   return dp[rod][rod]

def cut_rod_bu(prices, rod):
  dp = [0 for _ in range(rod + 1)]
  
  for i in range(1, rod+1):
    for j in range(1, i + 1): # the list of prices can't exceed the length of the rod
      dp[i] = max(dp[i], prices[j-1] + dp[i-j])
  return dp[rod]

if __name__ == "__main__":
  length = [1,2,3,4,5,6,7,8]
  prices = [1,5,8,9,10,17,17,20]
  rod = 4
  print("Max Rod price {}".format(cut_rod(length, prices, rod, rod-1)))
  print("Max Rod price {}".format(cut_rod2(prices, rod)))
  mem = [None] * (rod + 1)
  print("Max Rod price TD {}".format(cut_rod_td(prices, rod, mem)))
  print("Max Rod price {}".format(cut_rod_bu(prices, rod)))