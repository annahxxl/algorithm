def solution(my_string):
    check = set()
    answer = ''

    for s in my_string:
        if s not in check:
            check.add(s)
            answer += s
            continue
        
    return answer