def solution(clothes):
    dic = dict()
    for name, type in clothes:
        if type not in dic:
            dic[type] = 1
        else:
            dic[type] += 1
    
    answer = 1
    for count in dic.values():
        answer *= (count + 1) # 해당 종류의 의상을 입지 않는 경우 +1
    
    return answer - 1 # 모두 입지 않는 경우 -1