n, s, m = map(int, input().split())
volume_list = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1, n+1): # 노래
  for j in range(m+1): # 볼륨 정도
    if dp[i-1][j] == 0:
      continue
    if j - volume_list[i-1] >= 0:
      dp[i][j - volume_list[i-1]] = 1
    if j + volume_list[i-1] <= m:
      dp[i][j + volume_list[i-1]] = 1
result = -1
for i in range(m, -1, -1):
  if dp[n][i] == 1:
    result = i
    break
print(result)