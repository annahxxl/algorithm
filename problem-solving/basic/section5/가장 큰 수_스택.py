num, m = map(int, input().split())

num = str(num)

stack = []

for x in num:
  x = int(x)
  while stack and m>0 and stack[-1]<x:
    stack.pop()
    m -= 1
  stack.append(x)

if m != 0:
  stack = stack[:-m]
  
res = ''.join(map(str, stack))
  
print(res)