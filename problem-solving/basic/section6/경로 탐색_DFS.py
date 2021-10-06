def DFS(node):
  global cnt
  visited[node] = True
  path.append(node)
  if node == n:
    cnt += 1
    print('path{}:'.format(cnt), end=' ')
    for x in path:
      print(x, end=' ')
    print()
  else:
    for i in range(1, n + 1):
      if graph[node][i] == True and visited[i] == False:
        DFS(i)
        visited[i] = False
        path.pop()

if __name__ == '__main__':
  n, m = map(int, input().split())
  graph = [[False] * (n + 1) for _ in range(n + 1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
  visited = [False] * (n + 1)
  path = list()
  cnt = 0
  DFS(1)
  print(cnt)