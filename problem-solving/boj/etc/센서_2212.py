# k개의 덩어리로 분리한다고 생각하기
n = int(input())
k = int(input())
loc = list(map(int, input().split()))
if k > n :
  print(0) # 각 센서의 위치에 설치하면 되므로 정답은 0
else:
  loc.sort()
  distance = list() # 각 센서 간의 거리 저장
  for i in range(1, n):
    distance.append(loc[i] - loc[i-1])
  distance.sort(reverse=True)
  for i in range(k-1): # 가장 긴 거리부터 하나씩 제거
    distance[i] = 0 
  print(sum(distance))