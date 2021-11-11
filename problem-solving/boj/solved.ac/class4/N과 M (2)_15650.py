def DFS(idx, start):
  if idx == m:
    for num in combination:
      print(num, end=' ')
    print()
    return
  for i in range(start, n+1):
    combination[idx] = i
    DFS(idx+1, i+1)

if __name__ == '__main__':
  n, m = map(int, input().split())
  combination = [0] * m
  DFS(0, 1)