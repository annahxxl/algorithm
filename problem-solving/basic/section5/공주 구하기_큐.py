from collections import deque

n, k = map(int, input().split())

princes = deque(list(range(1, n+1)))

while princes:
  for _ in range(k-1):
    cur = princes.popleft() # 현재 외치는 사람
    princes.append(cur)
  princes.popleft() # k를 외치는 사람
  if len(princes) == 1:
    print(princes[0])
    break