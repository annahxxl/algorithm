def DFS(idx, total):
  global res
  if idx == n:
    if total > res:
      res = total
  else:
    if idx + times[idx] <= n:
      DFS(idx + times[idx], total + prices[idx]) # idx번째 상담을 하는 경우
    DFS(idx + 1, total) # idx번째 상담을 안 하는 경우

if __name__ == '__main__':
  n = int(input())
  times = []
  prices = []
  for _ in range(n):
    time, price = map(int, input().split())
    times.append(time)
    prices.append(price)
  res = -2147000000
  DFS(0, 0)
  print(res)