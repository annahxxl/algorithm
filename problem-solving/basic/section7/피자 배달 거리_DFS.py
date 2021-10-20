def DFS(idx, start):
  global res
  if idx == m:
    total = 0
    for x1, y1 in house:
      dis = 2147000000
      for i in combination:
        x2 = pizza[i][0]
        y2 = pizza[i][1]
        dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
      total += dis
    res = min(res, total)
  else:
    for i in range(start, len(pizza)): # 조합 구현
      combination[idx] = i
      DFS(idx + 1, i + 1)

if __name__ == '__main__':
  n, m = map(int, input().split())
  grid = [list(map(int, input().split())) for _ in range(n)]
  house = []
  pizza = []
  combination = [0] * m # 모든 피자집 중 m개를 선택하는 조합을 저장해 두는 리스트
  res = 2147000000
  for i in range(n):
    for j in range(n):
      if grid[i][j] == 1:
        house.append((i, j))
      elif grid[i][j] == 2:
        pizza.append((i, j))
  DFS(0, 0)
  print(res)