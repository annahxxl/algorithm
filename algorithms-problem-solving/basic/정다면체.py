n, m = map(int, input().split())
sum_cnt = [0] * (n+m) # 눈의 합을 카운트 해주는 리스트 (리스트의 index가 점수)
max = 0
# max = -2147000000

for i in range(1, n+1): # 눈의 합 횟수 저장
  for j in range(1, m+1):
    sum_cnt[i+j] += 1
    
for i in range(n+m+1): # 최대값 저장
  if sum_cnt[i] > max:
    max = sum_cnt[i]
    
for i in range(n+m+1): # 출력
  if sum_cnt[i] == max:
    print(i, end=' ')