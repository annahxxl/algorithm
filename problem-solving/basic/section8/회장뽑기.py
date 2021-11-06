# 플로이드 워샬 알고리즘
n = int(input())

dis = [[100] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신에서 자기 자신으로 가는 점수 초기화
  dis[i][i] = 0

while True: # 입력받은 친구 사이 점수 입력
  a, b = map(int, input().split())
  if a == -1 and b == -1:
    break
  dis[a][b] = 1
  dis[b][a] = 1

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

res = [0] * (n+1)
score = 100
for i in range(1, n+1):
  res[i] = max(dis[i][1:])
  score = min(score, res[i])

out = []
for i in range(1, n+1):
  if res[i] == score:
    out.append(i)

# 출력
print(score, len(out))
for x in out:
  print(x, end=' ')