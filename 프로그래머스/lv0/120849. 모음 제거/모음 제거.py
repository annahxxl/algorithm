def solution(my_string):
    answer = ''
    moeum = ['a', 'e', 'i', 'o', 'u']
    
    for s in my_string:
        if s not in moeum:
            answer += s
    
    return answer