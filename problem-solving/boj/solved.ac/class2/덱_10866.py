import sys
n = int(sys.stdin.readline())
DQ = []
for _ in range(n):
  command = sys.stdin.readline().split()
  if command[0] == 'push_front':
    DQ.insert(0, command[1])
  elif command[0] == 'push_back':
    DQ.append(command[1])
  elif command[0] == 'pop_front':
    if len(DQ) == 0:
      print(-1)
    else:
      print(DQ.pop(0))
  elif command[0] == 'pop_back':
    if len(DQ) == 0:
      print(-1)
    else:
      print(DQ.pop())
  elif command[0] == 'size':
    print(len(DQ))
  elif command[0] == 'empty':
    if len(DQ) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == 'front':
    if len(DQ) == 0:
      print(-1)
    else:
      print(DQ[0])
  elif command[0] == 'back':
    if len(DQ) == 0:
        print(-1)
    else:
      print(DQ[-1])