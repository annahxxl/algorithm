'''
# 병합 정렬 알고리즘을 이용한 풀이 O(NlogN)
def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])
  i, j, k = 0, 0, 0 # 왼쪽 포인터, 오른쪽 포인터, 합친 배열의 포인터
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k += 1
  if i == len(left):
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  elif j == len(right):
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
  return array

n = int(input())
array = list()
for _ in range(n):
  array.append(int(input()))
array = merge_sort(array)
for data in array:
  print(data)
'''

import sys
input = sys.stdin.readline
n = int(input())
lst = list()
for _ in range(n):
  lst.append(int(input()))
lst.sort()
for i in lst:
  print(i)