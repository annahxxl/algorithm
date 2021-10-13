# 해당 문제에서 아래와 같은 조건 때문에 뒤로 갈 수 없으므로 visited 리스트는 필요 없다.
# '구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록'

def DFS(x, y):
  global cnt
  if x == max_x and y == max_y:
    cnt += 1
  else:
    for dx, dy in direction:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < n and grid[x][y] < grid[nx][ny]:
        DFS(nx, ny)

if __name__ == '__main__':
  n = int(input())
  grid = [list(map(int, input().split())) for _ in range(n)]
  min_value = 2147000000
  max_value = -2147000000
  for i in range(n):
    for j in range(n):
      if grid[i][j] < min_value:
        min_value = grid[i][j]
        min_x = i
        min_y = j
      if grid[i][j] > max_value:
        max_value = grid[i][j]
        max_x = i
        max_y = j
  cnt = 0
  direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  DFS(min_x, min_y)
  print(cnt)