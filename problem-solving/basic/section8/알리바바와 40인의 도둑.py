# solution1: Bottom-up

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)] # dp[r][c] 까지의 최소 에너지를 저장하는 리스트
dp[0][0] = lst[0][0]
for i in range(1, n): # 첫 번째 행과 열 최소 에너지 저장
  dp[0][i] = dp[0][i-1] + lst[0][i]
  dp[i][0] = dp[i-1][0] + lst[i][0]

for i in range(1, n):
  for j in range(1, n):
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + lst[i][j]

print(dp[n-1][n-1])

'''
# solution2: Top-down

def DFS(x, y):
  if dp[x][y] > 0:
    return dp[x][y]
  if x == 0 and y == 0:
    return lst[0][0]
  else:
    if x == 0:
      dp[x][y] = DFS(x, y-1) + lst[x][y]
    elif y == 0:
      dp[x][y] = DFS(x-1, y) + lst[x][y]
    else:
      dp[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + lst[x][y]
    return dp[x][y]

if __name__ == '__main__':  
  n = int(input())
  lst = [list(map(int, input().split())) for _ in range(n)]
  dp = [[0] * n for _ in range(n)] # dp[r][c] 까지의 최소 에너지를 저장하는 리스트
  dp[0][0] = lst[0][0]
  print(DFS(n-1, n-1))
'''