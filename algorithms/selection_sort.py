def selection_sort(arr):
  for stand in range(len(arr)-1):
    lowest = stand # 기준점부터 가장 작은 값의 index
    for index in range(stand+1, len(arr)):
      if arr[lowest] > arr[index]:
        lowest = index 
    arr[lowest], arr[stand] = arr[stand], arr[lowest]
  return arr
  
import random
nums = random.sample(range(100), 10)
print(selection_sort(nums))