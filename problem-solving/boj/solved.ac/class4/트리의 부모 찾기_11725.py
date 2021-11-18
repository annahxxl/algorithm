from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

q = deque()
visited = [False] * (n+1)
parents = [0] * (n+1)
q.append(1)

while q:
  node = q.popleft()
  visited[node] = True
  for next in tree[node]:
    if not visited[next]: # if parents[i] == 0: 과 동일
      q.append(next)
      parents[next] = node

for i in range(2, n+1):
  print(parents[i])