def DFS(idx, start_value):
  global cnt
  if idx == m:
    cnt += 1
    for i in res:
      print(i, end=' ')
    print()
  else:
    for i in range(start_value, n + 1):
      res[idx] = i
      DFS(idx + 1, i + 1)

if __name__ == '__main__':
  n, m = map(int, input().split())
  res = [0] * m
  cnt = 0
  DFS(0, 1)
  print(cnt)