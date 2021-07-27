import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0
def dfs(i):
  visited[i] = True
  for j in range(1, n+1):
    if graph[i][j] == 1 and visited[j] == False:
      dfs(j)
for _ in range(m):
  u, v = map(int, input().split())
  graph[u][v] = 1
  graph[v][u] = 1
for i in range(1, n+1):
  if visited[i] == False:
    dfs(i)
    cnt += 1
print(cnt)