from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  q = deque([start])
  visited = [False] * (n + 1)
  cnt = 0
  while q:
    node = q.popleft()
    if not visited[node]:
      visited[node] = True
      cnt += 1
      for node in graph[node]:
        if not visited[node]:
          q.append(node)
  return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)
cnt = [0] * (n + 1)
for i in range(1, n+1):
  cnt[i] = bfs(i)
MAX = max(cnt)
for i in range(1, n+1):
  if cnt[i] == MAX:
    print(i, end=' ')