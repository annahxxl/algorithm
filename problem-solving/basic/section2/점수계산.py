n = int(input())
res = list(map(int, input().split()))
score = 0
cnt = 0

for num in res:
  if num == 1:
    cnt += 1
    score += cnt
  else:
    cnt = 0

print(score)