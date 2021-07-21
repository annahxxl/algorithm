# 분할 정복 알고리즘의 예

def binary_search(arr, search):
  if len(arr) == 1 and search == arr[0]:
    return True
  if len(arr) == 1 and search != arr[0]:
    return False
  if len(arr) == 0:
    return False
  
  mid = len(arr) // 2
  if search > arr[mid]:
    return binary_search(arr[mid+1:], search)
  else:
    return binary_search(arr[:mid], search)
  
import random
data_list = random.sample(range(100), 10)
data_list.sort()
print(data_list)
print(binary_search(data_list, 7))