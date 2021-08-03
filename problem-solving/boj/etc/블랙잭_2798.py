n, m = map(int, input().split())
cards = list(map(int, input().split()))
MAX = 0
for i in range(len(cards)):
  for j in range(i+1, len(cards)):
    for k in range(j+1, len(cards)):
      SUM = cards[i] + cards[j] + cards[k]
      if SUM <= m:
        MAX = max(MAX, SUM)
print(MAX)