'''
# my solution
n = int(input())
grid = list()
for _ in range(n):
  grid.append(list(map(int, input().split())))
SUM = list()
cross_sum_1 = cross_sum_2 = 0
for i in range(n):
  SUM.append(sum(grid[i])) # 행의 합
  cross_sum_1 += grid[i][i] # 대각선의 합
  cross_sum_2 += grid[i][n-i-1]
  col_sum = 0
  for j in range(n): # 열의 합
    col_sum += grid[j][i]
    SUM.append(col_sum)
SUM.append(cross_sum_1)
SUM.append(cross_sum_2)
print(max(SUM))
'''

# other solution
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
MAX = -2147000000
for i in range(n):
  row = col = 0 # 행의 합, 열의 합
  for j in range(n):
    row += grid[i][j]
    col += grid[j][i]
  if row > MAX:
    MAX = row
  if col > MAX:
    MAX = col
sum1 = sum2 = 0 # 대각선의 합
for i in range(n):
  sum1 += grid[i][i]
  sum2 += grid[i][n-i-1]
if sum1 > MAX:
    MAX = sum1
if sum2 > MAX:
  MAX = sum2
print(MAX)