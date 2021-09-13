'''
# my solution
essential = input()
n = int(input())
plan = [input() for _ in range(n)]
tmp = ''
for i in range(len(plan)):
  for j in plan[i]:
    if j in essential and j not in tmp:
      tmp += j
  if tmp == essential:
    print('#%d YES' %(i+1))
  else:
    print('#%d NO' %(i+1))
  tmp = ''
'''

# other solution
from collections import deque

need = input()
n = int(input())
for i in range(n):
  plan = input()
  dq = deque(need)
  for s in plan:
    if s in dq:
      if s != dq.popleft():
        break
  if len(dq) == 0:
    print('#%d YES' %(i+1))
  else:
    print('#%d NO' %(i+1))