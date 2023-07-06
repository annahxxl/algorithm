def solution(n, lost, reserve):
    answer = 0
    students = [1] * n
    
    for l in lost:
        students[l - 1] -= 1
    
    for r in reserve:
        students[r - 1] += 1

    for i in range(len(students)):
        if students[i] == 2:
            if i != 0 and students[i - 1] == 0:
                students[i - 1] += 1
                students[i] -= 1
                continue
            if i != n - 1 and students[i + 1] == 0:
                students[i + 1] += 1
                students[i] -= 1
    
    for s in students:
        if s > 0:
            answer += 1
    
    return answer