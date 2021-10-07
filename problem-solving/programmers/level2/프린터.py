from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    idx_q =  deque([i for i in range(0, len(priorities))])
    cnt = 0
    
    while priorities:
        if max(priorities) == priorities[0]:
            cnt += 1
            priorities.popleft()
            if location == idx_q.popleft(): # idx_q에서 popleft 적용과 동시에 비교
                return cnt
        else:
            priorities.append(priorities.popleft())
            idx_q.append(idx_q.popleft())