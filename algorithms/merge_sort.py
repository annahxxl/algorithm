  # 분할 정복 알고리즘 기법을 사용한 정렬 알고리즘 중 하나 (동적 게획법과 분할 정복 차이점 유의)
  
def merge(left, right):
  merged = list()
  left_point, right_point = 0, 0
  # case1: left 와 right 가 아직 남아있을 때
  while len(left) > left_point and len(right) > right_point:
    if left[left_point] > right[right_point]:
      merged.append(right[right_point])
      right_point += 1
    else:
      merged.append(left[left_point])
      left_point += 1
  # case2: left 만 남아있을 때
  while len(left) > left_point:
    merged.append(left[left_point])
    left_point += 1
  # case3: right 만 남아있을 때
  while len(right) > right_point:
    merged.append(right[right_point])
    right_point += 1
  return merged

def merge_split(arr):
  if len(arr) <= 1:
    return arr
  mid = int(len(arr)/2)
  left = merge_split(arr[:mid])
  right = merge_split(arr[mid:])
  return merge(left, right)

import random
data_list = random.sample(range(100), 10)
print(merge_split(data_list))