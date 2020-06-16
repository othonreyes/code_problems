"""
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

Related
https://www.techiedelight.com/partition-problem/
"""
### Naive approach
# def counter(fun):
#   calls = 0
#   def counter2(*args, **kwargs):
#     calls += 1
#     result = fun(*args, **kwargs)
#     print("Calls ", calls)
#     return result
#   return counter2


def subsetExists(set,sum):
  return ss(set, sum, 0)



def ss(set,sum, ix):
  print("."*10)
  if ix == len(set):
    print("Out of range: sum:{}, ix {}".format(sum, ix))
    return False
  if (sum == 0):
    return True
  print("sum:{}, ix {} val:{}".format(sum, ix, set[ix]))
  if (sum < 0):
    return False
  print("Good: sum:{}, ix {} val:{}".format(sum, ix, set[ix]))
  return ss(set, sum-set[ix], ix + 1) or ss(set, sum, ix + 1)

### DP top-down

def subsetExists_td(set,sum):
  n = len(set)
  mem = [[None for _ in range(sum + 1)] for _ in range(n+1)]
  return ss_td(set, sum, 0, mem)

def ss_td(set,sum, ix, mem):
  print("."*10)
  if ix == len(set):
    print("Out of range: sum:{}, ix {}".format(sum, ix))
    return False
  if (sum == 0):
    return True
  print("sum:{}, ix {} val:{}".format(sum, ix, set[ix]))
  if (sum < 0):
    return False
  if mem[ix][sum] is not None:
    return mem[ix][sum]
  print("Continue: sum:{}, ix {} val:{}".format(sum, ix, set[ix]))
  mem[ix][sum] = ss(set, sum-set[ix], ix + 1) or ss(set, sum, ix + 1)
  return mem[ix][sum]


def subsetExists_bu(set,sum):
  n = len(set)
  mem = [[False for _ in range(sum + 1)] for _ in range(n+1)]

  # Base case that is if the sum is zero i.e column 0, then the answer is true
  # there is a subset that makes it true
  for i in range(n+1):
    mem[i][0] = True

  # If sum is not 0 and set is empty,  
  # then answer is false  
  for i in range(1,sum+1): 
    mem[0][i]=False
  
  for i in range(1, n+1):
    for j in range(1, sum +1):
      if j<set[i-1] : # if the value in the set is bigger than the current sum then set the value to the previous value
        print("j:{} < set[i-1] {}".format(j, set[i-1]))
        mem[i][j] = mem[i-1][j]
      if j>=set[i-1]: # if not then there is a chance that we can find a subset
        print("j:{} >= {} =  mem[i-1][j]({}) or mem[i-1][j-set[i-1]]({})".format(j, set[i-1], mem[i-1][j], mem[i-1][j-set[i-1]]))
        mem[i][j] = mem[i-1][j] or mem[i-1][j-set[i-1]]
          # mem[i-1][j] = not use the value or mem[i-1][j-set[i-1]] use the value
  for i in range(n):
    print(mem[i])
  return mem[n][sum]

if __name__ == "__main__":
  set = [3, 34, 4, 12, 5, 2]
  sum = 9
  print(subsetExists(set,sum))
  print("#" * 50)
  print(subsetExists_td(set,sum))
  print("#" * 50)
  print(subsetExists_bu(set,sum))