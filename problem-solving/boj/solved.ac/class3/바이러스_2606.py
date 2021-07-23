# DFS
n = int(input()) # 컴퓨터의 수
m = int(input()) # 컴퓨터 쌍의 수
graph = dict()
for _ in range(m):
  a, b = map(int, input().split())
  if a not in graph: # 찾고자하는 키 in 딕셔너리
    graph[a] = [b]
  if b not in graph:
    graph[b] = [a]
  if a in graph:
    graph[a].append(b)
  if b in graph:
    graph[b].append(a)
need_visit = [1]
visited = list()
while need_visit:
  node = need_visit.pop()
  if node not in visited:
    if node in graph:
      visited.append(node)
      need_visit.extend(graph[node])
print(len(visited)-1)