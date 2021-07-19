import sys
input = sys.stdin.readline
m = int(input())
S = set()
for _ in range(m):
  command = input().split()
  if len(command) == 1:
    func = command[0]
    if func == 'all':
      S = set([i for i in range(1, 21)])
    elif func == 'empty':
      S = set()
  elif len(command) == 2:
    func, value = command[0], int(command[1])
    if func == 'add':
      S.add(value)
    elif func == 'remove':
      S.discard(value)
    elif func == 'check':
      if value in S:
        print(1)
      else:
        print(0)
    elif func == 'toggle':
      if value in S:
        S.remove(value)
      else:
        S.add(value)