def selection_sort(arr):
  n = len (arr)  
  for i in range(n):
    # find the smallest int    
    smallest = 9999999
    j_ix = i
    for j in range(i, n):
      if arr[j] < smallest:
        smallest = arr[j]
        j_ix = j
    # swap thems
    arr[j_ix], arr[i] = arr[i], arr[j_ix]
    

      

if __name__ == "__main__":
  arr = [5,9,1,2]
  print(arr)
  selection_sort(arr)
  print(arr)
  
  arr = [5,14,8,9,6,32,15,4,966,84,64,3,1,654,698,19,89]
  print(arr)
  selection_sort(arr)
  print(arr)