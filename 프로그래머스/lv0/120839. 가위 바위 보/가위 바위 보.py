def solution(rsp):
    win = {
        '0' : '5',
        '2' : '0',
        '5' : '2'
    }
    
    answer = ''
    
    for x in rsp:
        answer += win[x]
        
    return answer