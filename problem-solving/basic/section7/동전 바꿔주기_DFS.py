def DFS(idx, SUM):
  global res
  if SUM > t:
    return
  if idx == k:
    if SUM == t:
      res += 1
  else:
    for i in range(coin_cnt[idx] + 1): # 0개 부터 coin_cnt[idx]개까지
      DFS(idx + 1, SUM + (coin_type[idx] * i))

if __name__ == '__main__':
  t, k = int(input()), int(input())
  coin_type = []
  coin_cnt = []
  for _ in range(k):
    p, n = map(int, input().split())
    coin_type.append(p)
    coin_cnt.append(n)
  res = 0
  DFS(0, 0)
  print(res)