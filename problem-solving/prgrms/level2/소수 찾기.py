'''
# 시간 초과
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True    

def solution(numbers):
    answer = set()
    numbers = list(numbers)
    n = len(numbers)
    used = [False] * n
    res = 0
    
    def dfs(idx, num):
        if idx == n:
            if num != '':
                num = int(num)
                if is_prime(num):
                    answer.add(num)
        else:
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    dfs(idx + 1, num + numbers[i])
                    used[i] = False
                    dfs(idx + 1, num)
    
    dfs(0, '')

    return len(answer)
'''

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True    

def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numbers, i)) # i개씩 나열한 순열을 구해주는 메서드
        result = [int(''.join(i)) for i in p]
    
    for i in set(result):
        if is_prime(i):
            answer += 1
            
    return answer