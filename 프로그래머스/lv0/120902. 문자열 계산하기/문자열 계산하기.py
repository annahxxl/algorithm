def solution(my_string):
    my_string_list = my_string.split(' ')
    answer = int(my_string_list[0])
    op = '+'
    
    for i in range(1, len(my_string_list), 2):
        if my_string_list[i] == '+':
            answer += int(my_string_list[i + 1])
        else:
            answer -= int(my_string_list[i + 1])
    
    return answer