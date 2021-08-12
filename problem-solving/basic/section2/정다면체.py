n, m = map(int, input().split())
sums_cnt = [0] * (n+m+1) # index가 나올 수 있는 눈의 합
for i in range(1, n+1):
  for j in range(1, m+1):
    sum = i + j
    sums_cnt[sum] += 1
max_cnt = max(sums_cnt)
for i in range(len(sums_cnt)):
  if sums_cnt[i] == max_cnt:
    print(i, end=' ')