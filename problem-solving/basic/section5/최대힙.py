import heapq # 기본적으로 최소힙으로 작동

hq = list()
while True:
  n = int(input())
  if n == -1:
    break
  if n == 0:
    if hq:
      print(-heapq.heappop(hq))
    else:
      print(-1)
  else:
    heapq.heappush(hq, -n)