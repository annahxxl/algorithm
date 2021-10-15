from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
q = deque()

direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for i in range(n):
  for j in range(n):
    if grid[i][j] == 1:
      q.append((i, j))
      while q:
        x, y = q.popleft()
        grid[x][y] = 0
        for dx, dy in direction:
          nx, ny = x + dx, y + dy
          if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            q.append((nx, ny))
      cnt += 1

print(cnt)