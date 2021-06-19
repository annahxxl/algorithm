n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 회전
for _ in range(m):
  row, dir, size = map(int, input().split())
  if dir == 0: # 왼쪽 방향으로 회전할 경우
    for _ in range(size):
      grid[row-1].append(grid[row-1].pop(0))
  else: # 오른쪽 방향으로 회전할 경우
    for _ in range(size):
      grid[row-1].insert(0, grid[row-1].pop())
    
# 모래시계 합
res = 0
s = 0
e = n-1

for i in range(n):
  for j in range(s, e+1):
    res += grid[i][j]
  if i < n//2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1
    
print(res)