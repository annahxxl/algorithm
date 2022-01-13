def solution(numbers, target):
    cnt = 0
    
    def DFS(idx, total):
        nonlocal cnt

        if idx == len(numbers):
            if total == target:
                cnt += 1
        else:
            DFS(idx + 1, total + numbers[idx])
            DFS(idx + 1, total - numbers[idx])

    DFS(0, 0)
    
    return cnt