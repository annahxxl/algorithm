def DFS(x, y):
  visited[x][y] = True
  if x == 0:
    print(y)
  else: # 사다리 타기 이므로 좌, 우, 상 순으로 탐색
    if y - 1 >= 0 and grid[x][y - 1] == 1 and not visited[x][y - 1]:
      DFS(x, y - 1)
    elif y + 1 < 10 and grid[x][y + 1] == 1 and not visited[x][y + 1]:
      DFS(x, y + 1)
    else:
      DFS(x - 1, y)

if __name__ == '__main__':
  grid = [list(map(int, input().split())) for _ in range(10)]
  visited = [[False] * 10 for _ in range(10)]
  for y in range(10):
    if grid[9][y] == 2:
      DFS(9, y)