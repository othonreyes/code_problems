"""
https://www.techiedelight.com/subset-sum-problem/

"""

def subset_sum(items, target, n):
  if target == 0:
    return True
  if n<0:
    return False
  if target < 0:
    return False
  return subset_sum(items, target - items[n], n - 1) or \
    subset_sum(items, target, n - 1)

def subset_sum_2(items, target, n):
  if target == 0:
    return True
  if n<0:
    return False
  if target - items[n] < 0:
    return False
  return subset_sum(items, target - items[n], n - 1) or \
    subset_sum(items, target, n - 1)


def subset_sum_td(items, target, n, mem):
  """
  The key was to have target as the size of the array instead of the index.
  That makes sense because the value that we want to reuse is the target
  """
  if target == 0:
    return True
  if n<0 or target < 0:
    return False
  if mem[target] is not None:
    return mem[target]
  mem[target] =  subset_sum_td(items, target - items[n], n - 1, mem) or \
    subset_sum_td(items, target, n - 1, mem)
  return mem[target]


def subset_sum_bu(items, target):
  n = len(items)
  dp = [[False for _ in range(target + 1)] for _ in range(n+ 1)]
  
  # base case is that we found an answer
  for i in range(0, n + 1):
    dp[i][0] = True

  for i in range(1, n + 1):
    for j in range(target + 1):
      if j < items[i-1]:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j - items[i-1]] or dp[i-1][j]
  
  for i in range(0, n + 1):
    print(dp[i])
  return dp[n][target]
  

if __name__ == "__main__":
  items = [7, 3, 2, 5, 8] 
  target = 14
  print(subset_sum(items, target, len(items)-1))
  print(subset_sum_2(items, target, len(items)-1))
  mem = [None for _ in range(target + 1)]
  print(subset_sum_td(items, target, len(items)-1, mem))
  print(subset_sum_bu(items, target))