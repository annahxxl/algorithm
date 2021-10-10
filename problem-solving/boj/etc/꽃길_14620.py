n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]

direction = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)] # 현재 위치, 동, 남, 서, 북

res = 2147000000

def check(lst): # 세 개의 꽃의 위치들의 비용을 계산해 주는 함수
  cost = 0
  pos = []
  for flower in lst:
    row = flower // n
    col = flower % n
    if row == 0 or row == n - 1 or col == 0 or col == n - 1:
      return res
    for dx, dy in direction:
      cost += garden[row + dx][col + dy]
      pos.append((row + dx, col + dy))
  if len(set(pos)) != 15:
    return res
  return cost

for i in range(n * n):
  for j in range(n * n):
    for k in range(n * n):
      res = min(res, check([i, j, k]))

print(res)