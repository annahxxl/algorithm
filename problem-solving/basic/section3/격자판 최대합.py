n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

# # 격자 모양 출력
# for i in grid:
#   print(i)

# 행, 열의 합
for i in range(n):
  row = col = 0
  for j in range(n):
    row += grid[i][j]
    col += grid[j][i]
  if row > largest:
    largest = row
  if col > largest:
    largest = col
    
# 대각선의 합
cross1 = cross2 = 0
for i in range(n):
  cross1 += grid[i][i]
  cross2 += grid[i][n-i-1]
if cross1 > largest:
  largest = cross1
if cross2 > largest:
  largest = cross2
    
print(largest)