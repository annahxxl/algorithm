t = int(input())
for _ in range(t):
  log = input()
  left_stack = []
  right_stack = []
  for i in log:
    if i == '-':
      if left_stack:
        left_stack.pop()
    elif i == '<':
      if left_stack:
        right_stack.append(left_stack.pop())
    elif i == '>':
      if right_stack:
        left_stack.append(right_stack.pop())
    else:
      left_stack.append(i)
  left_stack.extend(reversed(right_stack)) # extend: 리스트 합치기, reversed: 리스트 요소를 역순으로 만들어 리턴
  print(''.join(left_stack))