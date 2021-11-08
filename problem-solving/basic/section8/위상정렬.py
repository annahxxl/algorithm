from collections import deque

n, m = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1) # idx(노드)의 진입차수 개수 저장하는 리스트

for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = True
  degree[b] += 1

q = deque()

for i in range(1, n+1):
  if degree[i] == 0:
    q.append(i)

while q:
  node = q.popleft()
  print(node, end=' ')
  for i in range(1, n+1):
    if graph[node][i]:
      degree[i] -= 1
      if degree[i] == 0:
        q.append(i)