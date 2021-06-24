t = int(input())

for _ in range(t):
  str = input()
  status = 0
  
  for i in str:
    if i == '(':
      status += 1
    elif i == ')':
      status -= 1
    if status < 0:
      print('NO')
      break
    
  if status > 0:
    print('NO')
  elif status == 0:
    print('YES')