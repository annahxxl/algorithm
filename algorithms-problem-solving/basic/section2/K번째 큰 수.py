n, k = map(int, input().split())
cards = list(map(int, input().split()))
sums = set()

for i in range(n):
  for j in range(i+1, n):
    for t in range(j+1, n):
      sums.add(cards[i] + cards[j] + cards[t]) # set자료구조는 add
      
sums = list(sums) # set자료구조는 중복❌, 순서❌ -> sort개념❌ -> 리스트로 바꿔야함
sums.sort(reverse = True)
print(sums[k-1])