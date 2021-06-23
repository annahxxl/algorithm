import heapq as hq # 기본적으로 최소힙으로 작동

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
      print(-hq.heappop(tree))
  else:
    hq.heappush(tree, -num)