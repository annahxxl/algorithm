n, m = map(int, input().split())

dis = [[5000] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신에서 자기 자신으로 가는 비용 초기화
  dis[i][i] = 0

for _ in range(m): # a에서 b로 가는 비용(c) 저장
  a, b, c = map(int, input().split())
  dis[a][b] = c

for k in range(1, n+1): # i에서 k를 거쳐 j(i > k > j)로 가는 최소 비용 저장 (플로이드 워샬 알고리즘)
  for i in range(1, n+1):
    for j in range(1, n+1):
      dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1): # 출력
  for j in range(1, n+1):
    if dis[i][j] == 5000:
      print('M', end=' ')
    else:
      print(dis[i][j], end=' ')
  print()