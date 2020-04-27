def bubble_sort(arr):
  n = len (arr)
  for i in range(n):
    for j in range(n):
      # if arr[i] > arr[j]: puts the biggest element at beginning
      if arr[i] < arr[j]: # puts smallest element at beginning
        arr[i], arr[j] = arr[j], arr[i]
        break

if __name__ == "__main__":
  arr = [5,9,1,2]
  print(arr)
  bubble_sort(arr)
  print(arr)
  
  arr = [5,14,8,9,6,32,15,4,966,84,64,3,1,654,698,19,89]
  print(arr)
  bubble_sort(arr)
  print(arr)
