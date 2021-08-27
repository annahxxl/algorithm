'''
# sol1
grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3): # 0~4, 1~5, 2~6
  for j in range(7):
    tmp = grid[j][i:i+5]
    if tmp == tmp[::-1]:
      cnt += 1
    for k in range(2):
      if grid[i+k][j] != grid[i+4-k][j]:
        break
    else:
      cnt += 1
print(cnt)
'''

# sol2
grid = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
  for j in range(3):
    if grid[i][j] == grid[i][j+4] and grid[i][j+1] == grid[i][j+3]:
      cnt += 1
    if grid[j][i] == grid[j+4][i] and grid[j+1][i] == grid[j+3][i]:
      cnt += 1
print(cnt)