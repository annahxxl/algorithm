# 위상 정렬 알고리즘을 이용한 풀이
'''
위상 정렬(Topology Sort) 알고리즘

1. 진입 차수가 0인 정점을 큐에 삽입합니다.
2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거합니다.
3. 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입합니다.
4. 큐가 빌 때까지 2-3 과정을 반복합니다.
'''
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1) 
heap = list()
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  indegree[y] += 1 # 진입 차수
for i in range(1, n+1): # 진입 차수가 0인 정점을 큐에 삽입
  if indegree[i] == 0:
    heapq.heappush(heap, i)
result = list()
while heap:
  # 큐에서 원소를 꺼내 해당 원소와 간선을 제거
  data = heapq.heappop(heap)
  result.append(data)
  for y in graph[data]:
    indegree[y] -= 1
    # 제거 이후 진입 차수가 0이 된 정점을 큐에 삽입
    if indegree[y] == 0:
      heapq.heappush(heap, y)
for i in result:
  print(i, end=' ')