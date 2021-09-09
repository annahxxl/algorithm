import heapq
import sys
input = sys.stdin.readline

n = int(input())
quiz = list()
for _ in range(n):
  d, c = map(int, input().split())
  quiz.append((d, c))
quiz.sort()
hq = list() # 최소 힙
for d, c in quiz:
  heapq.heappush(hq, c)
  if d < len(hq): # 데드라인을 초과하는 경우, 최소 컵라면의 개수 제거
    heapq.heappop(hq)
print(sum(hq))