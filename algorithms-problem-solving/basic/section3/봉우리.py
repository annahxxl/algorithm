n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 격자의 가장자리 0으로 초기화
grid.insert(0, [0]*n)
grid.append([0]*n)
for row in grid:
  row.insert(0, 0)
  row.append(0)

# 봉우리 세기
for i in range(1, n+1):
  for j in range(1, n+1):
      if grid[i][j] > max(grid[i-1][j], grid[i][j+1], grid[i+1][j], grid[i][j-1]):
        cnt += 1
        
# # sol2
# dx = [-1, 0, 1, 0] # 행 (상, 하)
# dy = [0, 1, 0, -1] # 열 (좌, 우)
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if all(grid[i][j]>grid[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt += 1
            
print(cnt)