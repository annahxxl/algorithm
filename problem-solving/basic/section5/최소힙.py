import heapq

hq = list()
while True:
  n = int(input())
  if n == -1:
    break
  if n == 0:
    if hq:
      print(heapq.heappop(hq))
    else:
      print(-1)
  else:
    heapq.heappush(hq, n)