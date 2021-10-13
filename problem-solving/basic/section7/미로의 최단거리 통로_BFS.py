from collections import deque

grid = [list(map(int, input().split())) for _ in range(7)]

q = deque()
visited = [[False] * 7 for _ in range(7)]

q.append((0, 0))
visited[0][0] = True
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
  x, y = q.popleft()
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < 7 and 0 <= ny < 7 and not visited[nx][ny] and grid[nx][ny] == 0:
      q.append((nx, ny))
      visited[nx][ny] = True
      grid[nx][ny] = grid[x][y] + 1

if grid[6][6] == 0:
  print(-1)
else:
  print(grid[6][6])