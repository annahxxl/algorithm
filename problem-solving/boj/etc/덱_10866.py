# 시간 초과 에러가 발생하므로
# 시간 단축을 위해 sys.stdin.readline()을 사용함
import sys

n = int(sys.stdin.readline())
queue = list()

for _ in range(n):
  comm = sys.stdin.readline().split()
  order = comm[0]
  
  if order == 'push_front':
    queue.insert(0, comm[1])
  elif order == 'push_back':
    queue.append(comm[1])
  elif order == 'pop_front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop(0))
  elif order == 'pop_back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop()) 
  elif order == 'size':
    print(len(queue))
  elif order == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif order == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif order == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])