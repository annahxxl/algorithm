# O(nlogn)
n = int(input())
nums = []
for _ in range(n):
  num = int(input())
  nums.append(num)
nums.sort()
for i in nums:
  print(i)

'''
# 선택 정렬 알고리즘으로 문제 해결하기 O(n**2)
n = int(input())
array = list()
for _ in range(n):
  array.append(int(input()))
for i in range(n):
  min_index = i # 가장 작은 원소의 index
  for j in range(i+1, n):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
for i in array:
  print(i)
'''