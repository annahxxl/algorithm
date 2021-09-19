def DFS(v):
  if v == n+1:
    for i in range(1, n+1):
      if used[i] == 1:
        print(i, end=' ')
    print()
  else:
    used[v] = 1
    DFS(v+1)
    used[v] = 0
    DFS(v+1)

if __name__ == '__main__':
  n = int(input())
  used = [0] * (n+1)
  DFS(1)