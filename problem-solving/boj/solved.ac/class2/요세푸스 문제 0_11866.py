from collections import deque
n, k = map(int, input().split())
p = deque(i+1 for i in range(n))
result = []
while p:
  for _ in range(k-1):
    p.append(p.popleft())
  result.append(p.popleft())
print('<', end='')
for i in range(len(result)-1):
  print(result[i], end=', ')
print(result[-1], end='')
print('>')