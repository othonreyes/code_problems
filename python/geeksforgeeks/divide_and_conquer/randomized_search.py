"""
https://www.geeksforgeeks.org/randomized-binary-search-algorithm/
"""

import random

def randomizedBinarySearch(arr, l,r, target):
  while l<=r:
    m = (l+random.randint(0, 10000)%(r-l+1))
    print(m)
    if arr[m] == x:
      return m
    if arr[m] > x:
      return randomizedBinarySearch(arr, l, m - 1, target)
    else:
      return randomizedBinarySearch(arr, m + 1, r, target)
  return -1

# Driver code  
if __name__=='__main__': 
    arr = [1, 2, 3, 4, 7, 9, 10,35, 38, 40] 
    n=len(arr) 
    x=10
    result = randomizedBinarySearch(arr, 0, n-1, x) 
    if result==-1: 
        print('Element is not present in array') 
    else: 
        print('Element is present at index ', result) 