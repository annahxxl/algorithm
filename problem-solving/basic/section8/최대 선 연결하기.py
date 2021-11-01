n = int(input())
lst = list(map(int, input().split()))

lst.insert(0, 0)
# 오른쪽의 번호 정보도 오름차순이어야 교차하지 않음 (최대 부분 증가수열 문제와 동일)
dp = [0] * (n + 1) # 가장 긴 증가 수열의 길이를 저장
dp[1] = 1
res = 0

for i in range(2, n + 1):
  max_len = 0
  for j in range(i - 1, 0, -1):
    if lst[j] < lst[i] and dp[j] > max_len:
      max_len = dp[j]
  dp[i] = max_len + 1
  res = max(res, dp[i])

print(res)