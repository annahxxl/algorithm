def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
                
    return answer

from collections import deque

def solution2(prices):
    prices = deque(prices)
    answer = []
    
    while prices:
        cur = prices.popleft()
        sec = 0
        for price in prices:
            sec += 1
            if cur > price:
                break 
        answer.append(sec)  
        
    return answer