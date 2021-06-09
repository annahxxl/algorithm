# N 구하기
cnt = int(input()) # N의 진짜 약수의 개수
nums = list(map(int, input().split())) # N의 진짜 약수들 (1과 N을 제외한 약수들)

nums = sorted(nums)

if cnt == 1:
  N = nums[0] ** 2
else:
  N = nums[1] * nums[-2]

print(N)