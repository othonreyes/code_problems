def search(arr, target):
  return search_rotated(arr, 0, len(arr)-1, target)

def search_rotated(arr, left, right, target):
  if right < left:
    return -1
  middle = (right + left) // 2
  if arr[middle] == target:
    return middle
  if arr[left] < arr[middle]:
    if arr[left] <= target and target < arr[middle]:
      return search_rotated(arr, left, middle - 1, target)
    else:
      return search_rotated(arr, middle + 1, right, target)
  else:
    if arr[right] >= target and target > arr[middle]:
      return search_rotated(arr, middle + 1, right, target)      
    else:
      return search_rotated(arr, left, middle - 1, target)
  


if __name__ == "__main__":
  arr = [11,12,13,45,1,2,3,5,6]
  print(search(arr,11))
  print(search(arr,45))
  print(search(arr,6))
  print(search(arr,9))