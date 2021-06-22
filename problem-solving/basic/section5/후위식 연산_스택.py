s = input()
stack = []

for x in s:
  if x.isdecimal():
    stack.append(int(x))
  elif x == '+':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2+n1)
  elif x == '-':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2-n1)
  elif x == '*':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2*n1)
  elif x == '/':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2/n1)
    
print(stack[0])