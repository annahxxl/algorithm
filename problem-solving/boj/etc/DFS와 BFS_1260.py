# DFS: 재귀함수나 스택을 이용하여 구현
# BFS: 큐를 이용하여 구현

from collections import deque

def DFS(v):
  print(v, end=' ')
  visited[v] = True
  for e in graph[v]:
    if not visited[e]:
      DFS(e)

def BFS(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if not visited[v]:
      visited[v] = True
      print(v, end=' ')
      for e in graph[v]:
        if not visited[e]:
          q.append(e)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for e in graph:
  e.sort()
visited = [False] * (n + 1)
DFS(v)
print()
visited = [False] * (n + 1)
BFS(v)