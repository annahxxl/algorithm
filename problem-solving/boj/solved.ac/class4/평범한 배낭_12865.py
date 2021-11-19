n, k = map(int, input().split())

dp = [0] * (k+1) # 배낭 무게의 한계값이 idx일 때 배낭속 물건의 최대가치를 저장하는 리스트

for _ in range(n):
  w, v = map(int, input().split())
  for i in range(k, w-1, -1):
    dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])