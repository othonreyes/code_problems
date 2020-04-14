# https://www.geeksforgeeks.org/window-sliding-technique/

def max_sum(arr, n, k):
  # find the max sum from 0 to k
  maxValue = 0
  for i in range(k):
    maxValue += arr[i]
  print("Max sum from 0 to k:" + str(maxValue))

  start = 0
  temp = maxValue
  for i in range(k,n):
    temp = temp + arr[i] - arr[start]
    # if temp > maxValue :
    #   maxValue = temp
    maxValue = max(temp, maxValue) 
    print(str(maxValue) + "- " + str(temp))
    start+=1
  return maxValue

arr = [5,6,7,10,47,-5,8,27,6]
k = 3
n = len(arr)
result = max_sum(arr, n, k) 
print("MAx value was ", result)