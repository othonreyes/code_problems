# Time: O(n)
# Source https://www.geeksforgeeks.org/rearrange-array-arri/
"""
Visit all the elements in the array and store them in a map
Then iterate again to create the result, if it is in the map then add the number otherwise -1
"""

def rearrange(arr, n):
  result = list()
  seen = {}

  for i in range(n):
    seen[str(arr[i])] = i
  print(seen)
  
  for i in range(n):
    val = i if (seen.get(str(i)) is not None) else -1
    print(val)
    result.append(val)
  return result

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)
print(rearrange(arr, n))