direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def DFS(x, y):
  global cnt
  cnt += 1
  grid[x][y] = 0
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
      DFS(nx, ny)

if __name__ == '__main__':
  n = int(input())
  grid = [list(map(int, input())) for _ in range(n)]
  
  cnt = 0
  res = []
  
  for i in range(n):
    for j in range(n):
      if grid[i][j] == 1:
        cnt = 0
        DFS(i, j)
        res.append(cnt)
  
  print(len(res))
  res.sort()
  for x in res:
    print(x)