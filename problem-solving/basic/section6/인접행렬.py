# 가중치 방향 그래프

n, m = map(int, input().split())

# 방향 그래프 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b, cost = map(int, input().split())
  graph[a][b] = cost

# 출력
for i in range(1, n + 1):
  for j in range(1, n + 1):
    print(graph[i][j], end=' ')
  print()

'''
# 무방향 그래프일 경우

n, m = map(int, input().split())

# 무방향 그래프 초기화
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True
'''