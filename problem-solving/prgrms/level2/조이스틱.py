def solution(name):
    cnt = 0
    next = 0
    min_move = len(name) - 1
    
    for idx, char in enumerate(name):
        cnt += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, idx + idx + len(name) - next)
    
    return cnt + min_move