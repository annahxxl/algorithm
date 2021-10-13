def DFS(x, y):
  global cnt
  grid[x][y] = 1
  if x == 6 and y == 6:
    cnt += 1
  else:
    for dx, dy in direction:
      nx, ny = x + dx, y + dy
      if 0 <= nx < 7 and 0 <= ny < 7 and grid[nx][ny] == 0:
        grid[nx][ny] = 1
        DFS(nx, ny)
        grid[nx][ny] = 0

if __name__ == '__main__':
  grid = [list(map(int, input().split())) for _ in range(7)]
  cnt = 0
  direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  DFS(0, 0)
  print(cnt)