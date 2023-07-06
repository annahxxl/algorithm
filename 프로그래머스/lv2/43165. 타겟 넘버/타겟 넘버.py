def dfs(depth, numbers, total, target):
    cnt = 0
    
    if depth == len(numbers):
        if total == target:
            cnt += 1
        return cnt
    
    cnt += dfs(depth + 1, numbers, total + numbers[depth], target)
    cnt += dfs(depth + 1, numbers, total - numbers[depth], target)
    
    return cnt

def solution(numbers, target):
    answer = dfs(0, numbers, 0, target)
    return answer