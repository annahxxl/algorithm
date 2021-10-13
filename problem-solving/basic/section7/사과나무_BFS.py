from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque() # 방문해야 할 좌표를 저장하는 큐
visited = [[False] * n for _ in range(n)]
res = 0

tmp = n // 2
q.append((tmp, tmp))
visited[tmp][tmp] = True
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
  x, y = q.popleft()
  res += grid[x][y]
  if x == 0 and y == tmp:
    break
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
      q.append((nx, ny))
      visited[nx][ny] = True

'''
# solution 2
res += grid[tmp][tmp]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
depth = 0

while True:
  if depth == tmp:
    break
  for i in range(len(q)):
    x, y = q.popleft()
    for dx, dy in direction:
      nx, ny = x + dx, y + dy
      if not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
        res += grid[nx][ny]
  depth += 1
'''

print(res)