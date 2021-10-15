from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque()
dist = [[False] * m for _ in range(n)]
res = 0

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(n):
  for j in range(m):
    if grid[i][j] == 1:
      q.append((i, j))

while q:
  x, y = q.popleft()
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
      q.append((nx, ny))
      grid[nx][ny] = 1 # 익은 표시
      dist[nx][ny] = dist[x][y] + 1
      res = max(res, dist[nx][ny])

all_red = True # 상자 안의 토마토가 모두 익었는지

for i in range(n):
  for j in range(m):
    if grid[i][j] == 0:
      all_red = False
      break

if not all_red:
  print(-1)
else:
  print(res)