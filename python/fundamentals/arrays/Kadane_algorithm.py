"""
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""

def maxSubArraySum(a, n):
  maxElem = 0
  maxArr = 0
  for i in range(n):
    maxElem = maxElem + a[i]
    if maxElem < 0:
      maxElem = 0
    if maxElem > maxArr:
      maxArr = maxElem
  return maxArr

def maxSubArraySumSimpler(a, n):
  maxElem = 0
  maxArr = 0
  for i in range(n):
    maxElem = maxElem + a[i]
    maxElem = max(maxElem, 0)
    maxArr = max(maxArr, maxElem)
  return maxArr

if __name__ == "__main__":
  a = [-2, -3, 4, -1, -2, 1, 5, -3] 
  print("Maximum contiguous sum is", maxSubArraySum(a,len(a))) 
  print("Maximum contiguous sum is", maxSubArraySumSimpler(a,len(a))) 