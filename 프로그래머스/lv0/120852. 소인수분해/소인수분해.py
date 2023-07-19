def solution(n):
    answer = set()
    num = n
    
    for i in range(2, n + 1):
        while num % i == 0:
            num = num // i
            answer.add(i)
                
    return sorted(list(answer))