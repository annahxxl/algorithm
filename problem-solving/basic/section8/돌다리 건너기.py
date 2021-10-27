# Bottom-up
n = int(input())
dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 2):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n + 1])

'''
# Top-down
def DFS(step):
  if dp[step] > 0:
    return dp[step]
  if step == 1 or step == 2:
    return step
  else:
    dp[step] = DFS(step - 1) + DFS(step - 2)
    return dp[step]

if __name__ == '__main__':
  n = int(input())
  dp = [0] * (n + 2)
  dp[1] = 1
  dp[2] = 2
  print(DFS(n + 1))
'''