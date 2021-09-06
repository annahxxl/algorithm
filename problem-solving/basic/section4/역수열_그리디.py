'''
# sol1
n = int(input())
arr = list(map(int, input().split()))
result = [0] * (n + 1)
for i in range(1, n+1):
  for j in range(1, n+1):
    if arr[i-1] == 0 and result[j] == 0:
      result[j] = i
      break
    elif result[j] == 0:
      arr[i-1] -= 1 # 앞에 만들어야 할 빈 자리 수 check
for i in range(1, n+1):
  print(result[i], end=' ')
'''

# sol2
n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
res = list()
for i in arr:
  res.insert(i, n)
  n -= 1
for i in res:
  print(i, end=' ')