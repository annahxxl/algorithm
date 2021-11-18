n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

cost.insert(0, [0]*3)
dp = [[0]*3 for _ in range(1001)]
r, g, b = 0, 1, 2
dp[1] = [cost[1][r], cost[1][g], cost[1][b]]

for i in range(2, n+1):
  dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + cost[i][r]
  dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + cost[i][g]
  dp[i][b] = min(dp[i-1][r], dp[i-1][g]) + cost[i][b]

print(min(dp[n]))