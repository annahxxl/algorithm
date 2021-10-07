def DFS(idx, score, time):
  global res
  if time > m:
    return
  if idx == n:
    if score > res:
      res = score
  else:
    DFS(idx + 1, score + scores[idx], time + times[idx]) # idx번 문제를 풀 경우
    DFS(idx + 1, score, time) # idx번 문제를 안 풀 경우

# solution 2 - 조합 이용하여 풀기
def DFS2(start_idx, score, time):
  global res
  if time > m:
    return
  if score > res:
    res = score
  for i in range(start_idx, n):
    DFS2(i + 1, score + scores[i], time + times[i])

if __name__ == '__main__':
  n, m = map(int, input().split())
  scores = []
  times = []
  for _ in range(n):
    score, time = map(int, input().split())
    scores.append(score)
    times.append(time)
  res = -2147000000
  DFS(0, 0, 0)
  print(res)