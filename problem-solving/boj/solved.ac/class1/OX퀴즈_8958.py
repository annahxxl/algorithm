T = int(input())

for _ in range(T):
  answer = input()
  score = 0
  cnt = 0
  for i in answer:
    if i == 'O':
      cnt += 1
      score += cnt
    else:
      cnt = 0
  print(score)