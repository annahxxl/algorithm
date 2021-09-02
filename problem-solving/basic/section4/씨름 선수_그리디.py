'''
# my solution
n = int(input())
player = list()
for _ in range(n):
  height, weight = map(int, input().split())
  player.append((height, weight))
player.sort() # 1) 키 순서로 정렬
cnt = 0
MAX = 0
for i in range(n): # 2) 몸무게 비교
  MAX = player[i][1]
  for j in range(i+1, n):
    weight = player[j][1]
    if weight > MAX:
      break
  else:
    cnt += 1
print(cnt)
'''

# other solution
n = int(input())
player = list()
for _ in range(n):
  height, weight = map(int, input().split())
  player.append((height, weight))
player.sort(reverse=True)
MAX = 0
cnt = 0
for height, weight in player:
  if weight > MAX:
    MAX = weight
    cnt += 1
print(cnt)