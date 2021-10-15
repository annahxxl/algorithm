def solution(lottos, win_nums):
    answer = []
    zero = 0
    cnt = 0
    
    for i in lottos:
        if i == 0:
            zero += 1
            continue
        if i in win_nums:
            cnt += 1
    
    for i in range(2):
        if i == 0:
            res = cnt + zero
        else:
            res = cnt
        if res == 6:
            answer.append(1)
        elif res == 5:
            answer.append(2)
        elif res == 4:
            answer.append(3)
        elif res == 3:
            answer.append(4)    
        elif res == 2:
            answer.append(5)
        else:
            answer.append(6)
            
    return answer

def solution2(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    ans = 0
    
    for x in win_nums:
        if x in lottos:
            ans += 1
    
    return [rank[ans + zero], rank[ans]]