"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the 
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights 
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum 
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an
 item, either pick the complete item, or don’t pick it (0-1 property).

V = [60,100,120]
W = [10,20,30]
Weight = 50
Output  = 220
"""
def knapsack(V,W,Weight,n):
  if n < 0 or Weight == 0:
    return 0
  if W[n-1] > Weight: # Ignore the current n
    return knapsack(V,W,Weight,n - 1)
  return max(V[n-1] + knapsack(V,W,Weight - W[n-1],n - 1), knapsack(V,W,Weight - W[n-1],n - 1))

def knapsack_td(V,W,Weight,n):
  mem = [None] * (Weight + 1)
  return knapsack_td_rec(V,W,Weight,n, mem)

def knapsack_td_rec(V,W,Weight,n, mem):
  if n < 0 or Weight == 0:
    return 0
  if mem[Weight]:
    return mem[Weight]
  if W[n-1] > Weight: # Ignore the current n
    return knapsack_td_rec(V,W,Weight,n - 1, mem)
  mem[Weight] = max(V[n-1] + knapsack_td_rec(V,W,Weight - W[n-1],n - 1, mem), knapsack_td_rec(V,W,Weight - W[n-1],n - 1, mem))
  return mem[Weight]

def knapsack_bu(V,W,Weight,n):
  """
  The mem is a matrix of the number of items (rows) vs weight(cols) so it's huge.
  Here the important thing is the relationship of the weight and the matrix.
  Each column represents a given weight. The value in the ith and jth postion represents
  the max value that we can get out of the ith item and at the current weight jth.

  Then the conditions:
  if the weight of the ith item is too large, then pick the value of the previous row
  because it's like saying "I don't want the value of this item, i rather the previous one"

  If the weight of the ith item is still allowed so (weight(ith)<jth) then we
  want to pick the maximum value between not picking this item or picking this item and 
  the max value of the previous item but at a j-Weight(ith) position.
  """
  mem = [[0 for _ in range(Weight+1)] for _ in range(n+1)]
  
  for i in range(1,n+1): # iterate over the items as they are the rows
    for j in range(W[i-1],Weight+1): # iterate over the columns
      if W[i-1] > j: # if the weight of the item is too big then carry over the previous value
        mem[i][j] = mem[i-1][j]
      else:
        mem[i][j] = max( V[i-1] + mem[i-1][j - W[i-1]], mem[i-1][j])
    print("{}".format(mem[i]))
  return mem[n][Weight]

if __name__ == "__main__":
  V = [60,100,120]
  W = [10,20,30]
  Weight = 50
  n = len(V)
  print(knapsack(V,W,Weight,n))
  print(knapsack_td(V,W,Weight,n))
  print(knapsack_bu(V,W,Weight,n))
