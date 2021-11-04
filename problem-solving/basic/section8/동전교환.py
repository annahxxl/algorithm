# 냅색 알고리즘
n = int(input())
coins = list(map(int, input().split()))
m = int(input())

dp = [500] * (m+1) # 거슬러 줄 돈이 idx일 때 동전의 최소개수를 저장하는 리스트
dp[0] = 0

for coin in coins:
  for j in range(coin, m+1):
    dp[j] = min(dp[j], dp[j-coin] + 1)

print(dp[m])