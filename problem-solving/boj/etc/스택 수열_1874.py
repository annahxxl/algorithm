n = int(input())
cnt = 1
log = []
stack = []
for _ in range(n):
  num = int(input())
  while cnt <= num:
    log.append('+')
    stack.append(cnt)
    cnt += 1
  if stack[-1] == num:
    log.append('-')
    stack.pop()
  else:
    print('NO')
    break
else:
  # for i in log:
  #   print(i)
  print('\n'.join(log)) # '구분자'.join(리스트)