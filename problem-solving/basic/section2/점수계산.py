n = int(input())
result = map(int, input().split())
cnt = 0
score = 0
for i in result:
  if i == 1:
    cnt += 1
    score += cnt
  else:
    cnt = 0
print(score)