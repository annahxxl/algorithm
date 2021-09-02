'''
# my solution
from collections import deque

def bfs(start):
  cnt = 0
  q = deque([start])
  while q:
    node = q.popleft()
    if not visited[node]:
      visited[node] = True
      cnt += 1
      for node in graph[node]:
        q.append(node)
  return (cnt - 1)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
print(bfs(1))
'''

# other solution
# 컴퓨터의 수가 적으므로, DFS를 이용해 빠르게 문제를 푸는 것이 유리
# 일반적으로 BFS, DFS 둘 다 이용할 수 있는 경우 BFS 선호
def dfs(now):
  global cnt
  cnt += 1
  visited[now] = True
  for next in graph[now]:
    if not visited[next]:
      dfs(next)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
cnt = 0
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
dfs(1)
print(cnt - 1)