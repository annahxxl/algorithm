cards = list(range(21))

for _ in range(10):
  s, e = map(int, input().split())
  for i in range((e-s+1)//2):
    cards[s+i], cards[e-i] = cards[e-i], cards[s+i]
    
for i in range(1, 21):
  print(cards[i], end=' ')