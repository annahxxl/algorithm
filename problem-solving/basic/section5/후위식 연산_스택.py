ex = input()
stack = list()
for s in ex:
  if s.isdigit():
    stack.append(int(s))
  elif s == '+':
    a = stack.pop()
    b = stack.pop()
    stack.append(b + a)
  elif s == '-':
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)
  elif s == '*':
    a = stack.pop()
    b = stack.pop()
    stack.append(b * a)
  elif s == '/':
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)
print(stack[0])