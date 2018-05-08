def qsortLomuto(nums, start, end):
  if start >= end:
    return
  p = partitionLomuto(nums, start, end)
  qsortLomuto(nums, start, p-1)
  qsortLomuto(nums, p+1, end)

def partitionLomuto(nums, start, end):
  pivot = nums[end]
  i = start
  for j in range(start, end):
    if nums[j] < pivot:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
  nums[i], nums[end] = nums[end], nums[i]
  return i

def qsortHoare(nums, start, end):
  if start >= end:
    return
  p = partitionHoare(nums, start, end)
  qsortHoare(nums, start, p)
  qsortHoare(nums, p+1, end)
  
def partitionHoare(nums, start, end):
  pivot = nums[start]
  l = start - 1
  r = end + 1
  while True:
    while True:
      l += 1
      if nums[l] >= pivot:
        break
    while True:
      r -= 1
      if nums[r] <= pivot:
        break
    if l >= r:
      return r
    nums[l], nums[r] = nums[r], nums[l]

    
nums = [3, 2, 5, 1, 5]
n = len(nums)
qsortLomuto(nums, 0, n-1)
print(nums)

nums = [3, 2, 5, 1, 5]
qsortHoare(nums, 0, n-1)
print(nums)