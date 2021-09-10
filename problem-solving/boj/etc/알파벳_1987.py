def bfs(x, y):
  res = 0
  q = set() # 동일한 경우는 한 번만 계산하기 위해 set 자료형 사용
  q.add((x, y, board[x][y]))
  while q:
    x, y, step = q.pop()
    res = max(res, len(step))
    # 네 방향 (상, 하, 좌, 우)으로 이동하는 경우를 각각 확인
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx = x + dx
      ny = y + dy
      # 이동할 수 있는 위치이면서, 새로운 알파벳인 경우
      if 0 <= nx and nx < r and 0 <= ny and ny < c and board[nx][ny] not in step:
        q.add((nx, ny, step + board[nx][ny]))
  return res

r, c = map(int, input().split())
board = list()
for _ in range(r):
  board.append(input())
print(bfs(0, 0))