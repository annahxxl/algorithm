import sys

def DFS(idx, SUM):
  if idx == n and SUM == f:
    for i in origin:
      print(i, end=' ')
    sys.exit()
  else:
    for i in range(1, n + 1):
      if used[i] == False:
        used[i] = True
        origin[idx] = i
        DFS(idx + 1, SUM + (i * cnt[idx]))
        used[i] = False

if __name__ == '__main__':
  n, f = map(int, input().split())
  origin = [0] * n
  used = [False] * (n + 1)
  cnt = [1] * n
  for i in range(1, n): # 이항계수 적용
    cnt[i] = cnt[i-1] * (n - i) // i
  DFS(0, 0)