from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    cnt = 0
    
    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1
        else:
            people.pop()
            cnt += 1
    
    return cnt