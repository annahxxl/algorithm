n = int(input())
loc = []
for _ in range(n):
  x, y = map(int, input().split(' '))
  loc.append((x, y))
  
loc.sort(key=lambda x: (x[0], x[1]))

for i in loc:
  print(i[0], i[1])