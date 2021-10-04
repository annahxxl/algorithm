from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    days_left = deque()
    for i in range(len(progresses)):
        progress_left = 100 - progresses[i]
        day_left = math.ceil(progress_left / speeds[i])
        days_left.append(day_left)

    deadline = days_left.popleft()
    cnt = 1
    while days_left:
        next_deadline = days_left.popleft()
        if deadline >= next_deadline:
            cnt += 1
        else:
            answer.append(cnt)
            deadline = next_deadline
            cnt = 1
    answer.append(cnt)

    return answer

def solution2(progresses, speeds):
    answer = []
    
    time = 0
    count = 0
    while progresses:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    
    return answer