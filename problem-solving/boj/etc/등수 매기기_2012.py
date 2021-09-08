n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
res = 0
for i in range(n):
  res += abs((i+1) - arr[i])
print(res)