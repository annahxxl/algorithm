import sys

t = int(sys.stdin.readline())

for _ in range(t):
  words = list(map(list, sys.stdin.readline().split()))
  for i in words:
    print(''.join(i[::-1]), end=' ')