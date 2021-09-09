ex = input()
stack = list()
res = ''
for s in ex:
  if s.isdigit():
    res += s
  else:
    if s == '(':
      stack.append(s)
    elif s == '*' or s == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(s)
    elif s == '+' or s == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(s)
    elif s == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()
while stack:
  res += stack.pop()
print(res)