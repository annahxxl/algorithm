from collections import deque

def bfs():
  q = deque([n])
  while q:
    now = q.popleft() # 현재 위치
    if now == k:
      return time[now]
    for next in (now-1, now+1, now*2):
      if 0 <= next < MAX and time[next] == 0: # 해당 위치를 방문하지 않았다면
        time[next] = time[now] + 1
        q.append(next)

n, k = map(int, input().split())
MAX = 100001
time = [0] * 100001 # index 위치까지 가는 시간
print(bfs())