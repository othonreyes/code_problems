def twoSum(nums, target):
  n = len(nums)
  if n < 2:
      return list()
  
  visited = {}
  for i in range(0,n):
    diff = target - nums[i]
    j = visited.get(str(diff), None)
    if j is not None and not (i == j):
        return [i, j]
    visited[str(nums[i])] = i
  return list()
      
nums = [2,7,15,19]
result = twoSum(nums, 9)
print(result)