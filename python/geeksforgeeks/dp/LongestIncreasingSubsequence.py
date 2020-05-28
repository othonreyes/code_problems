"""
The longest increasing subsequence problem is to find a subsequence of a given
 sequence in which the subsequence’s elements are in sorted order, lowest to 
 highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.
 https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/
"""

def longestIncreasingSubsequence(input):
  n = len (input)
  return lis_rec(input, 0, n, -9999)

def lis_rec(input, ix, n, prev):
  if (ix == n):
    return 0
  a = lis_rec(input, ix + 1, n, prev)
  b = 0
  if prev < input[ix]:
    b = lis_rec(input, ix + 1, n, input[ix]) + 1
  val = max(a,b)
  print("{}-{}".format(ix, val))
  return val

def lis_td(input):
  n = len(input)
  mem = [None]*(n+1)
  return lis_rec_td(input, 0, n, -9999, mem)
"""
didn't work: to use memoization we need to iterate starting from the end of the array
https://stackoverflow.com/questions/37561909/does-there-exist-a-top-down-dynamic-programming-solution-for-longest-increasing
"""
def lis_rec_td(input, ix, n, prev, mem):
  if (ix == n):
    return 0
  if mem[ix]:
    return mem[ix]
  a = lis_rec_td(input, ix + 1, n, prev, mem)
  b = 0
  if prev < input[ix]:
    b = lis_rec_td(input, ix + 1, n, input[ix], mem) + 1
  mem[ix] = max(a,b)
  return mem[ix]

def lis_bu(input):
  n = len(input)
  L = [0]*(n+1)
  L[0] = 1
  max_val = 0
  for i in range(1,n):
    for j in range(i):
      if L[j]>L[i] and input[i] > input[j]:
        L[i] = L[j]
    L[i] += 1
    max_val = max(max_val, L[i])
  return max_val

# def lis_rec(input, ix, n, count):
#   if (ix == n):
#     return count
#   a = lis_rec(input, ix + 1, n, count)
#   b = 0
#   if input[ix-1]<input[ix]:
#     b = lis_rec(input, ix + 1, n, count + 1)
#   else:
#     b = lis_rec(input, ix + 1, n, count)
#   return max(a,b)


if __name__ == "__main__":
  input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
  print(longestIncreasingSubsequence(input))
  print(lis_td(input))
  print(lis_bu(input))