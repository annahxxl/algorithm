n = int(input())
points = list()
for _ in range(n):
  x, y = map(int, input().split())
  points.append((x, y))
# point.sort(key=lambda x: (x[0], x[1])) # 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬
points = sorted(points) # sort로 하면 시간 초과 발생,, 왜일까,,
for x, y in points:
  print(x, y)