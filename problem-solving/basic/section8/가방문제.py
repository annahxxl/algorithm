# 냅색 알고리즘
n, m = map(int, input().split())

dp = [0] * (m+1) # 무게의 한계값이 idx일 때 보석의 최대가치를 저장하는 리스트

for i in range(n):
  w, v = map(int, input().split())
  for j in range(w, m+1):
    dp[j] = max(dp[j], dp[j-w] + v)

print(dp[m])