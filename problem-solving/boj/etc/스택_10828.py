# 시간 초과 에러가 발생하므로
# 시간 단축을 위해 sys.stdin.readline()을 사용함
import sys

n = int(sys.stdin.readline())
stack = list()

for _ in range(n):
  comm = sys.stdin.readline().split()
  order = comm[0]
  
  if order == 'push':
    stack.append(comm[1])
  elif order == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif order == 'size':
    print(len(stack))
  elif order == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif order == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])