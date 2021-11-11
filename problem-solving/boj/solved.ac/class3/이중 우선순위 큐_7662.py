import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
  min_hq, max_hq = [], []
  keys = [False] * 1000000
  
  for key in range(int(input())):
    command, num = input().split()
    num = int(num)
    
    if command == 'I':
      heapq.heappush(min_hq, (num, key))
      heapq.heappush(max_hq, (-num, key))
      keys[key] = True
    elif command == 'D':
      if num == 1:
        while max_hq and not keys[max_hq[0][1]]:
          heapq.heappop(max_hq)
        if max_hq:
          keys[max_hq[0][1]] = False
          heapq.heappop(max_hq)
      else:
        while min_hq and not keys[min_hq[0][1]]:
          heapq.heappop(min_hq)
        if min_hq:
          keys[min_hq[0][1]] = False
          heapq.heappop(min_hq)
    
  while max_hq and not keys[max_hq[0][1]]:
    heapq.heappop(max_hq)
  while min_hq and not keys[min_hq[0][1]]:
    heapq.heappop(min_hq)
  
  if max_hq and min_hq:
    print(-max_hq[0][0], min_hq[0][0])
  else:
    print('EMPTY')