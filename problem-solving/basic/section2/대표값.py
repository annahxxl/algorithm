n = int(input())
scores = list(map(int, input().split()))
# avg = round(sum(scores)/n) # 파이썬에서 round는 round_half_even 방식이므로 아래 방법으로 수정
avg = int(sum(scores)/n + 0.5)
min_diff = 2147000000
for i in range(n):
  diff = abs(avg-scores[i])
  if diff < min_diff:
    min_diff = diff
    result = i+1
    score = scores[i]
  elif diff == min_diff:
    if score < scores[i]:
      score = scores[i]
      result = i+1
print(avg, result)