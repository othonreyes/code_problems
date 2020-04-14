# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# Time: O(n)
# Space: 1
def reverseByMiddles(arr):
  n = len(arr)
  limit = n//2

  for i in range(limit):
    temp = arr[i]
    arr[i] = arr[(n-1)-i]
    arr[(n-1)-i] = temp
  return arr

arr = [1,2,3]
result = reverseByMiddles(arr)
print(result)

print(reverseByMiddles(arr = [1,2,3,4]))

