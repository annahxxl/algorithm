n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n # nums[idx]까지의 가장 긴 증가수열의 길이를 저장하는 리스트

for i in range(1, n):
  for j in range(i):
    if nums[j] < nums[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))