# 계수 정렬 알고리즘을 사용한 풀이
import sys
input = sys.stdin.readline
n = int(input())
nums = [0] * 10001
for _ in range(n):
  num = int(input())
  nums[num] += 1
for i in range(10001):
  if nums[i] != 0:
    for j in range(nums[i]):
      print(i)