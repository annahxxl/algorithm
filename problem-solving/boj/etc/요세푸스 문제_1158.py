import sys

n, k = map(int, sys.stdin.readline().split())
circle = list([i for i in range(1, n+1)])
res = [] # 제거된 사람들 넣을 배열
idx = 0 # 제거될 사람의 인덱스 번호

for i in range(len(circle)):
  idx += k-1
  if idx >= len(circle):
    idx = idx % len(circle)
    
  res.append(circle.pop(idx))

  # 리스트 안의 각 항목이 정수형이라면 문자열로 변환해주어야 join 메소드 사용 가능
print('<', ', '.join(map(str, res)), '>', sep='')