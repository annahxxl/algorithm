def solution(array, commands):
    answer = []
    for command in commands:
        result = sorted(array[command[0]-1 : command[1]])
        answer.append(result[command[2]-1])
    return answer