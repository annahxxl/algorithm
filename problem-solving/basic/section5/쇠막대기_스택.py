ex = input()
cnt = 0
stack = list() # 잘릴 쇠막대기
for i in range(len(ex)):
  if ex[i] == ')':
    stack.pop()
    if ex[i-1] == '(': # 레이저
      cnt += len(stack)
    else: # 쇠막대기 끝부분
      cnt += 1
  else:
    stack.append(ex[i])
print(cnt)