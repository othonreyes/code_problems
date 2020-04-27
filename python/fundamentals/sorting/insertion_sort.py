def insertion_sort(arr):
  n = len (arr)  
  for i in range(1, n):
    # if the element in the position is smaller than the last element of the 
    # already sorted array then
    if arr[i] < arr[i-1]:
      # resort the array by storing the new highest value
      temp = arr[i]
      for j in range(0,i):
        if temp < arr[j]:
          arr[j], temp = temp, arr[j]
      arr[i] = temp
      

if __name__ == "__main__":
  arr = [5,9,1,2]
  print(arr)
  insertion_sort(arr)
  print(arr)
  
  arr = [5,14,8,9,6,32,15,4,966,84,64,3,1,654,698,19,89]
  print(arr)
  insertion_sort(arr)
  print(arr)