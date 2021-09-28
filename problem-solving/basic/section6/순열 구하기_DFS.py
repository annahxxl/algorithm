def DFS(idx):
  global cnt
  if idx == m:
    cnt += 1
    for i in res:
      print(i, end=' ')
    print()
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        res[idx] = i
        DFS(idx + 1)
        ch[i] = 0

if __name__ == '__main__':  
  n, m = map(int, input().split())
  res = [0] * m
  ch = [0] * (n + 1)
  cnt = 0
  DFS(0)
  print(cnt)