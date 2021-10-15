import sys
sys.setrecursionlimit(10 ** 6)

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def DFS(x, y, h):
  visited[x][y] = True
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > h:
      DFS(nx, ny, h)

if __name__ == '__main__':
  n = int(input())
  grid = [list(map(int, input().split())) for _ in range(n)]
  
  cnt = 0
  res = 0
  
  for h in range(1, 101): # 장마철 비의 높이
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if not visited[i][j] and grid[i][j] > h:
          DFS(i, j, h)
          cnt += 1
    if cnt == 0:
      break
    res = max(res, cnt)
    
  print(res)