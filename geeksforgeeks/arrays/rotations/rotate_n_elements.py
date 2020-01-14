# Rotate to the left
# Method 1: Coppying the results to another array
# T: O(n)
# M: O(n)
def rotate(arr, d):
  r = []
  start = len(arr) - d
  for i in range(len(arr)):
    r.append(arr[start])
    start+=1
    if start == len(arr):
      start = 0
  return r
arr = [1,2,3,4,5,6,7]
print(rotate(arr, 2))

# Method 2: Rotate 1 to the right
# [1,2,3,4,5,6,7]
# [7,1,2,3,4,5,6]
# [6,7,1,2,3,4,5]
def rotateToRight(arr, n, d):  
  for i in range(d):
    rotateOneToTheRight(arr, n)
  return arr

def rotateOneToTheRight(arr, n):
  last = arr[n-1]
  a = arr[0]
  b =0
  for i in range(1, n):
    b = arr[i]
    arr[i] = a
    a = b
  arr[0] = last

arr = [1,2,3,4,5,6,7]
n = len(arr)
print(rotateToRight(arr, n,  3))

# Method 2: Rotate 1 to left one by one
def rotateToLeft(arr, n, d):  
  for i in range(d):
    rotateOneToTheLeft(arr, n)
  return arr


def rotateOneToTheLeft(arr, n):
  last = arr[0]
  for i in range(n-1):
    arr[i] = arr[i+1]
  arr[n-1] = last

arr = [1,2,3,4,5,6,7]
n = len(arr)
print(rotateToLeft(arr, n,  5))


# Method 4: Reverse rotation
# source https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
# [1,2,3,4,5,6,7] n =7, d=2
# Rotate:
#   reverse(arr, 0, d-1) [2,1,3,4,5,6,7] 
#   reverse(arr, d, n-1) [2,1,7,6,5,4,3] 
#   reverse(arr, 0, n-1) [3,4,5,6,7,1,2] 
def reverseRotate(arr, n, d):
  reverse(arr, 0, d-1)
  reverse(arr, d, n-1)
  reverse(arr, 0, n-1)
  return arr
def reverse(arr, start, end):
  # This is a classic revers algorithm between 2 ends.
  while(start<end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start +=1
    end -=1

arr = [1,2,3,4,5,6,7]
n = len(arr)
d = 2
print(reverseRotate(arr,n,d))
