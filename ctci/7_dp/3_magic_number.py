def mn_unique(arr):
  return mn(arr, 0, len(e) - 1)

def mn(arr, s=0,e):
  if e<s:
    return -1
  m = (s + e) // 2
  if arr[m] == m:
    return m
  if arr[m] < m:
    return mn(arr, s, m)
  else: 
    return mn(arr, m, e)

def mn_repeated(arr, s=0,e):
  if e<s:
    return -1
  m = (s + e) // 2
  if arr[m] == m:
    return m

  left = min(mid - 1, arr[m])
  lv = mn_repeated(arr, s, left)
  if lv > -1:
    return lv
  
  right = max(mid + 1, arr[m])
  rv = mn_repeated(arr, right, end)
  if rv > -1:
    return rv
  return -1

if __name__ == "__main__":
  arr = [-10, -5, -1, 1,2,3,5, 7, 9, 12, 13]
  arr = [-10, -5, 2, 2,2,3,4,5, 9, 12, 13]