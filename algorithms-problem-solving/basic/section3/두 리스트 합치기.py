n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
p1 = p2 = 0 # 각 리스트의 포인터
res = []

while p1<n and p2<m:
  if first[p1] <= second[p2]:
    res.append(first[p1])
    p1 += 1
  else:
    res.append(second[p2])
    p2 += 1
    
if p1 < n:
  res = res + first[p1:]

if p2 < m:
  res = res + second[p2:]
  
for i in res:
  print(i, end=' ')