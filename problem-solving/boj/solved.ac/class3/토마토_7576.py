from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      q.append((i, j))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
  x, y = q.popleft()
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
      q.append((nx, ny))
      box[nx][ny] = box[x][y] + 1

res = 0
all_red = True

for i in range(n):
  for j in range(m):
    if box[i][j] == 0:
      all_red = False
      break
    res = max(res, box[i][j])

if all_red:
  print(res-1)
else:
  print(-1)