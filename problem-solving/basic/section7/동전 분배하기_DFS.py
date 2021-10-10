def DFS(idx):
  global res
  if idx == n:
    if len(set(money)) == 3:
      diff = max(money) - min(money)
      if diff < res:
        res = diff
  else:
    for i in range(3):
      money[i] += coin[idx]
      DFS(idx + 1)
      money[i] -= coin[idx]

if __name__ == '__main__':
  n = int(input())
  coin = [int(input()) for i in range(n)]
  money = [0] * 3
  res = 2147000000
  DFS(0)
  print(res)