# 퀵 정렬은 분할 정복 알고리즘의 대표적인 예 (동적 게획법과 분할 정복 차이점 유의)

def qsort(arr):
  if len(arr) <= 1:
    return arr
  
  left, right = list(), list()
  pivot = arr[0]
  
  for i in range(1, len(arr)):
    if pivot > arr[i]:
      left.append(arr[i])
    else:
      right.append(arr[i])

  return qsort(left) + [pivot] + qsort(right)

# 위 퀵정렬 코드를 파이썬 list comprehension을 사용해서 더 깔끔하게 작성해보기 (pythonic)
def qsort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  
  left = [item for item in arr[1:] if pivot > item]
  right = [item for item in arr[1:] if pivot <= item]
  
  return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100), 10)
print(qsort(data_list))