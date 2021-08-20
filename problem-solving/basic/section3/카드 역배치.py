cards = [i for i in range(1, 21)]
for _ in range(10):
  a, b = map(int, input().split())
  for i in range((b-a+1)//2):
    cards[a-1+i], cards[b-1-i] = cards[b-1-i], cards[a-1+i]
for i in cards:
  print(i, end=' ')