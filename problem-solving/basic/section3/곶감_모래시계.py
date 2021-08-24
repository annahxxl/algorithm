n = int(input())
yard = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
order = [list(map(int, input().split())) for _ in range(m)]
for i in range(len(order)): # 회전
  row, direction, size = order[i]
  if direction == 0:
    for _ in range(size):
      yard[row-1].append(yard[row-1].pop(0))
  else:
    for _ in range(size):
      yard[row-1].insert(0, yard[row-1].pop())
s = 0
e = n-1
result = 0
for i in range(n):# 출력
  result += sum(yard[i][s:e+1])
  if i < n // 2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1
print(result)