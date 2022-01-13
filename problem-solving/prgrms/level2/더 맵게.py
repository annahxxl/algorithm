import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        cnt += 1
        
    return cnt