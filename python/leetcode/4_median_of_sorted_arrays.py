def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  n1 = len(nums1)
  n2 = len(nums2)
  
  nums = []
  i = 0
  j = 0
  while i < n1 or j < n2:
    if i < n1 and j <n2:
      if nums1[i] < nums2[j]:
        nums.append(nums1[i])
        i +=1 
      elif nums1[i] > nums2[j]:
        nums.append(nums2[j])
        j += 1 
      else:
        nums.append(nums1[i])
        nums.append(nums2[j])
        i +=1 
        j += 1 
    elif i< n1:
      nums.append(nums1[i])
      i +=1 
    else:
      nums.append(nums2[j])
      j += 1 
  
  n = len(nums)
  if n % 2 == 0:
    return (nums[n//2] + nums[n//2-1]) / 2
  else:
    return nums[n//2]
    
    
    