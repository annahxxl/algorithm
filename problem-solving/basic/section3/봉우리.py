'''
# my solution
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
grid.insert(0, [0]*n)
grid.append([0]*n)
for i in range(n+2):
  grid[i].insert(0, 0)
  grid[i].append(0)
cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i+1][j]:
      cnt += 1
print(cnt)
'''

# other solution
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
grid.insert(0, [0]*n)
grid.append([0]*n)
for i in grid:
  i.insert(0, 0)
  i.append(0)

cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if all(grid[i][j] > grid[i+dx[k]][j+dy[k]] for k in range(4)): # all(조건식): 조건식이 모두 만족될 때 True
      cnt += 1

print(cnt)