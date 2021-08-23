n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
s = e = mid = n // 2
result = 0
for i in range(n):
  result += sum(farm[i][s:e+1])
  if i < mid:
    s -= 1
    e += 1
  else:
    s += 1
    e -= 1
print(result)