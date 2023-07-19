def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    return 1

def solution(n):
    for i in range(2, 11):
        result = factorial(i)
        if result == n:
            return i
        if result > n:
            return i - 1