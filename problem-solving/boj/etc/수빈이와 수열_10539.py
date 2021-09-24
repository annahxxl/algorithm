n, b = int(input()), list(map(int, input().split()))

a = list()
for i in range(1, n+1):
  a.append(b[i-1] * i - sum(a))

for i in a:
  print(i, end=' ')