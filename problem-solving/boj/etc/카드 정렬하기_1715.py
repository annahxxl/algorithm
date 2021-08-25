import heapq
n = int(input())
heap = list()
for _ in range(n):
  data = int(input())
  heapq.heappush(heap, data)
result = 0
while len(heap) > 1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  SUM = one + two
  result += SUM
  heapq.heappush(heap, SUM)
print(result) 