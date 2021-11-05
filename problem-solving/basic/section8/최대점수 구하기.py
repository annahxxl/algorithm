# 냅색 알고리즘
n, m = map(int, input().split())

dp = [0] * (m+1) # 제한 시간이 idx일때 최대 점수를 저장하는 리스트

for _ in range(n):
  score, time = map(int, input().split())
  for j in range(m, time-1, -1):
    dp[j] = max(dp[j], dp[j-time] + score)

print(dp[m])