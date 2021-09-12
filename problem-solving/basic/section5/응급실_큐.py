'''
# my solution
from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
wait = deque()
for i in range(n):
  wait.append((i, danger[i]))
cnt = 0
while True:
  idx, danger = wait.popleft()
  for p, d in wait:
    if danger < d:
      wait.append((idx, danger))
      break
  else:
    cnt += 1
    if idx == m:
      print(cnt)
      break
'''

# other solution
from collections import deque

n, m = map(int, input().split())
q = deque([(pos, val) for pos, val in enumerate(list(map(int, input().split())))]) # enumerate: 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
cnt = 0
while True:
  cur = q.popleft()
  if any(cur[1] < x[1] for x in q):
    q.append(cur)
  else:
    cnt += 1
    if cur[0] == m:
      print(cnt)
      break