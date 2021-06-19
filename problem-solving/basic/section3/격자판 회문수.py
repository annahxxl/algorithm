grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
  for j in range(3):
    # 행 별 체크
    tmp = grid[i][j:j+5]
    if tmp == tmp[::-1]:
      cnt += 1
    # 열 별 체크
    for k in range(2):
      if grid[j+k][i] != grid[j+4-k][i]:
        break
    else:
      cnt += 1

print(cnt)