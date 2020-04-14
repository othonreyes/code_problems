# https://www.geeksforgeeks.org/count-of-subarrays-having-exactly-k-distinct-elements/
# Given an array arr[] of size N and an integer K. The task is to find the count of subarrays such that each subarray has exactly K distinct elements.
#
#  Input: arr[] = {2, 1, 2, 1, 6}, K = 2
# Output: 7
# {2, 1}, {1, 2}, {2, 1}, {1, 6}, {2, 1, 2},
# {1, 2, 1} and {2, 1, 2, 1} are the only valid subarrays.

# Input: arr[] = {1, 2, 3, 4, 5}, K = 1
# Output: 5
# O(n)^2
def explore(arr, start, n, k):
  numFound = {}
  count = 0
  for i in range(start, n):
    index = str(arr[i])
    # print("--" + index)
    numFound[index] = True
    if len(numFound) > k:
      return count
    elif len(numFound) == k:
      count+=1
      # print("Array found from {" + str(start)+ ", " + str(i) + "}. Count " + str(count)) 
  return count

def search(arr, n, k):
  arrsFound = 0
  for i in range(n):
     found = explore(arr, i, n, k)
     arrsFound += found
    #  print("Arrays found " + str(found) + ". Total so far " + str(arrsFound))
  return arrsFound

# O(n) * 2
def exactlyK(arr, n, k):
  return atMost(arr, n, k) - atMost(arr, n, k-1)

# EL approach es contar cuantos subarrays posibles hay con HASTA "K" elementos. 
# En otras palabras, cuantos subarrays posibles(permutaciones) existen donde haya de 1 hasta K elementos
# Esos nos da el numero total de subarrays. Despues, obtenemos el numero total de subarrays que tengan
# de a hsata K-1. por que k-1? porque asi eliminas subarrays que no tengan exactamente K elementos.

def atMost(arr, n, k):
  count = 0 
  left = 0 
  right = 0 
  map = {}
  while right < n:
    iRight = str(arr[right])
    map[iRight] = map.get(iRight, 0) + 1
    while len(map) > k:
      iLeft = str(arr[left])
      map[iLeft] = map[iLeft] - 1
      if map[iLeft] == 0:
        del map[iLeft]
      left +=1
    count += right - left + 1
    right+=1

  return count

arr = [2, 1, 2, 1, 6]
k = 2
n = len(arr)
print(str(search(arr,n, k)))
print(str(exactlyK(arr,n, k)))


arr = [1,2,3,4,5]
k = 1
n = len(arr)
print(str(search(arr,n, k)))
print(str(exactlyK(arr,n, k)))
