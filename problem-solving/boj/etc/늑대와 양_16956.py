r, c = map(int, input().split())
farm = [list(input()) for _ in range(r)]

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

check = False # 늑대가 양이 있는 칸으로 갈 수 있는지의 여부

for i in range(r):
  for j in range(c):
    if farm[i][j] == 'W':
      for dx, dy in direction:
        nx, ny = i + dx, j + dy
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
          continue
        if farm[nx][ny] == 'S':
          check = True

if check:
  print(0)
else:
  print(1)
  for i in range(r):
    for j in range(c):
      if farm[i][j] not in 'SW':
        farm[i][j] = 'D'
  for row in farm:
    print(''.join(row))