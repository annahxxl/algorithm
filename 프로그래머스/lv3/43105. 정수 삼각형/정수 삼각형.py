def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [row for row in triangle]

    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] += triangle[i - 1][j - 1]
            else:
                dp[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
    return max(dp[-1])