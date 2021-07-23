# 재귀 깊이가 1000 이상 깊어질 경우 Maximum recursion depth excced 런타임 에러가 발생할 수 있음
import sys
sys.setrecursionlimit(100000)

# DFS
t = int(input())

def dfs(i, j):
  if i<0 or i>=n or j<0 or j>=m:
    return
  if field[i][j] == 0:
    return
  field[i][j] = 0 # 방문한 배추는 0으로 갱신
  # 상하좌우 탐색
  dfs(i, j+1)
  dfs(i, j-1)
  dfs(i-1, j)
  dfs(i+1, j)
  
for _ in range(t):
  m, n, k = map(int, input().split()) # 가로 길이, 세로 길이, 배추가 심어져 있는 위치의 개수
  field = [[0]*m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    field[y][x] = 1 # 배추 위치 표시
  count = 0 # 지렁이 수
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1 # dfs 종료하면 지렁이 수 추가
  print(count)