def solution(numbers):
    answer = 0
    n = len(numbers)
    
    for i in range(n):
        for j in range(i + 1, n):
            answer = max(answer, numbers[i] * numbers[j])
    
    return answer