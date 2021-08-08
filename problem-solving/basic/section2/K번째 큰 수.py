n, k = map(int, input().split())
cards = list(map(int, input().split()))
result = set()
for i in range(1, n):
  for j in range(i+1, n):
    for t in range(j+1, n):
      result.add(cards[i] + cards[j] + cards[t])
result = sorted(result, reverse=True)
print(result[k-1])