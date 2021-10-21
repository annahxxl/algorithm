# Bottom-up
n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])

'''
# Top-down (재귀 & 메모이제이션)
def DFS(len):
  if dp[len] > 0:
    return dp[len]
  if len == 1 or len == 2:
    return len
  else:
    dp[len] = DFS(len - 1) + DFS(len - 2)
    return dp[len]

if __name__ == '__main__':
  n = int(input())
  dp = [0] * (n + 1)
  print(DFS(n))
'''