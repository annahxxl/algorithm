import heapq as hq # 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와주는 모듈

tree = []

while True:
  num = int(input())
  if num == -1:
    break
  elif num == 0:
    if len(tree) == 0:
      print(-1)
      break
    else:
      print(hq.heappop(tree))
  else:
    hq.heappush(tree, num)