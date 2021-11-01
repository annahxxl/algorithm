n = int(input())
bricks = []
for _ in range(n):
  s, h, w = map(int, input().split())
  bricks.append((s, h, w))

bricks.sort(reverse=True)
dp = [0] * n # idx번째의 벽돌이 맨 위에 있을 경우 최대 높이를 저장하는 리스트
dp[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
  max_h = 0
  for j in range(i - 1, -1, -1):
    if bricks[j][2] > bricks[i][2] and dp[j] > max_h:
      max_h = dp[j]
  dp[i] = max_h + bricks[i][1]
  res = max(res, dp[i])

print(res)