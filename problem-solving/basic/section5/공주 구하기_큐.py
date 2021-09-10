from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
while q:
  for _ in range(k-1):
      q.append(q.popleft())
  q.popleft()
  if len(q) == 1:
    print(q.pop())