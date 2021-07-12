# 시간 초과
# import sys

# n = sys.stdin.readline()
# nums1 = list(map(int, sys.stdin.readline().split()))
# m = sys.stdin.readline()
# nums2 = list(map(int, sys.stdin.readline().split()))

# for num in nums2:
#   if num in nums1:
#     print(1)
#   else:
#     print(0)

# 이분 탐색
n = int(input())
nums1 = sorted(list(map(int, input().split(' '))))
m = int(input())
nums2 = list(map(int, input().split(' ')))

def binary_search(target, array):
  start = 0 # 시작 인덱스
  end = n-1 # 마지막 인덱스
  pointer = (start + end) // 2 # 현재 포인터가 가르키고 있는 인덱스
  
  while start <= end:
    if array[pointer] == target:
      return 1
    elif array[pointer] < target:
      start = pointer + 1
    else:
      end = pointer - 1
    pointer = (start + end) // 2
  return 0

for i in range(len(nums2)):
  print(binary_search(nums2[i], nums1))