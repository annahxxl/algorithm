from collections import deque

n, m = map(int, input().split())
weight = deque(sorted(list(map(int, input().split()))))
cnt = 0
while weight:
  if len(weight) >= 2 and weight[0] + weight[-1] <= m:
    weight.popleft()
    weight.pop()
    cnt += 1
  else:
    weight.pop()
    cnt += 1
print(cnt)