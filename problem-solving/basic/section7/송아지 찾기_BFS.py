from collections import deque

s, e = map(int, input().split())
MAX = 10000
cnt = [0] * (MAX + 1) # 각각의 좌표 점으로 가는 최소 점프 수를 저장하는 리스트
visited = [False] * (MAX + 1)
q = deque()

q.append(s)
visited[s] = True
while q:
  now = q.popleft() # 현재 위치
  if now == e:
    break
  else:
    for next in (now - 1, now + 1, now + 5):
      if 0 < next and next <= MAX and not visited[next]:
        q.append(next)
        visited[next] = True
        cnt[next] = cnt[now] + 1

print(cnt[now])