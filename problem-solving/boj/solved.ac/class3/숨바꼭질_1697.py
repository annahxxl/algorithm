from collections import deque
def bfs(n, k):
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    if x == k:
      print(dist[x])
      return
    for next in (x-1, x+1, x*2):
      if 0 <= next < MAX and dist[next] == 0:
        dist[next] = dist[x] + 1
        q.append(next)
n, k = map(int, input().split())
MAX = 100001
dist = [0] * MAX
bfs(n, k)