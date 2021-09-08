# 다익스트라 알고리즘 이용 (최단 경로)
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
  heap = list()
  heapq.heappush(heap, (start, 0)) # (정점, 비용)
  distance[start] = 0
  while heap:
    now, dist = heapq.heappop(heap) # 현재 노드, 거리
    if distance[now] < dist:
      continue
    for node in graph[now]:
      cost = dist + node[1]
      if distance[node[0]] > cost:
        distance[node[0]] = cost
        heapq.heappush(heap, (node[0], cost))

t = int(input())
for _ in range(t):
  n, m, start = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  distance = [1e9] * (n + 1)
  for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[y].append((x, cost))
  dijkstra(start)
  cnt = 0 # 감염된 컴퓨터 수
  last = 0 # 마지막 컴퓨터까지 감염되는 시간
  for i in distance:
    if i != 1e9:
      cnt += 1
      if i > last:
        last = i
  print(cnt, last)