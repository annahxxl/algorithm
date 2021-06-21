n = int(input())
body = []

for _ in range(n):
  height, weight = map(int, input().split())
  body.append((height, weight))
  
body.sort(reverse=True)

largest = 0 # 몸무게 최대값
cnt = 0

for height, weight in body:
  if weight > largest:
    cnt += 1
    largest = weight
    
print(cnt)