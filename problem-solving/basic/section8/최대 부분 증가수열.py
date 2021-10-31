n = int(input())
lst = list(map(int, input().split()))

lst.insert(0, 0)
dp = [0] * (n + 1) # 가장 긴 증가 수열의 길이를 저장
dp[1] = 1
res = 0

for i in range(2, n + 1):
  maximum = 0
  for j in range(i - 1, 0, -1):
    if lst[j] < lst[i] and dp[j] > maximum:
      maximum = dp[j]
  dp[i] = maximum + 1
  if dp[i] > res:
    res = dp[i]

print(res)

'''
# solution 2
n = int(input())
lst = list(map(int, input().split()))

max_list = [0] * (max(lst) + 1)

for num in lst:
  max_list[num] = max(max_list[:num]) + 1

print(max(max_list))
'''