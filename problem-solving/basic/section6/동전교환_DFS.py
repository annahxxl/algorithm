def DFS(depth, total): # 해당 동전을 사용할 개수, 현재까지 거슬러준 값
  global res
  if depth >= res:
    return
  if total > m:
    return
  if total == m:
    if depth < res:
      res = depth
  else:
    for i in coin:
      DFS(depth+1, total+i)

if __name__ == '__main__':
  n = int(input())
  coin = list(map(int, input().split()))
  m = int(input())
  res = 2147000000
  coin.sort(reverse=True)
  DFS(0, 0)
  print(res)