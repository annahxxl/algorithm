def solution(s):
    answer = ''
    dic = {}
    
    for char in s:
        dic[char] = dic.get(char, 0) + 1
        
    for key, value in dic.items():
        if value == 1:
            answer += key

    return ''.join(sorted(answer))