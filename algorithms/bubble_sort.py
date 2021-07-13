def bubble_sort(arr):
  for i in range(len(arr)-1): # 턴 수
    swap = False # 한번이라도 정렬이 발생하면 True
    for j in range(len(arr)-1-i): # 비교 index, 한 턴 돌때마다 맨 뒤값 고정
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap = True
    if swap == False:
      break
  return arr
    
import random
nums = random.sample(range(100), 50)
print(bubble_sort(nums))