def DFS(idx, SUM):
  global res
  if idx == k:
    if 0 < SUM and SUM <= s:
      res.add(SUM)
  else:
    DFS(idx + 1, SUM + weights[idx]) # idx번째 추를 왼쪽에 놓을 경우
    DFS(idx + 1, SUM - weights[idx]) # idx번째 추를 오른쪽에 놓을 경우
    DFS(idx + 1, SUM) # idx번째 추를 사용하지 않을 경우

if __name__ == '__main__':
  k = int(input())
  weights = list(map(int, input().split()))
  s = sum(weights)
  res = set()
  DFS(0,0)
  print(s - len(res))