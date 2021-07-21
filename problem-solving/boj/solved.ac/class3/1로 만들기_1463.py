# 다이나믹 프로그래밍
n = int(input())
dp = [0 for _ in range(n+1)] # 계산 최소 횟수 저장을 위한 DP 테이블
for i in range(2, n+1):
  dp[i] = dp[i-1] + 1 # 현재의 수에서 1을 빼는 경우
  if i%2 == 0: # 현재의 수가 2로 나누어 떨어지는 경우
    dp[i] = min(dp[i], dp[i//2]+1)
  if i%3 == 0: # 현재의 수가 3으로 나누어 떨어지는 경우
    dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])