def solution(participant, completion):
    answer = ''
    dic = {}
    # 참가자 딕셔너리에 등록
    for person in participant:
        if person not in dic:
            dic[person] = 1
        else:
            dic[person] += 1
    # 완주자 표시
    for person in completion:
        if person in dic:
            dic[person] -= 1
    # 동명이인까지 고려하여 완주자가 아닐 경우 0이 아닌 값 체크
    for person in participant:
        if dic[person] != 0:
            answer = person            
    return answer