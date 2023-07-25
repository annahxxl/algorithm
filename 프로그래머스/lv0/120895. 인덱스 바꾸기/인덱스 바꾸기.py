def solution(my_string, num1, num2):
    my_string_list = list(my_string)
    tmp = my_string_list[num1]
    my_string_list[num1] = my_string_list[num2]
    my_string_list[num2] = tmp
    return ''.join(my_string_list)