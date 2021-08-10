def solution(n, lost, reserve):
    answer = 0
    check = [1 for _ in range(n+1)]
    for i in lost:
        check[i] = 0 # 체육복 없는 학생 체크
    checked_reserve = set(reserve[:]) # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 확인, 시간 복잡도 고려하여 set 자료형 사용
    for i in reserve:
        if i in lost:
            check[i] = 1 
            checked_reserve.discard(i)
    for i in checked_reserve:
        if i == n:
            if check[i-1] == 0:
                check[i-1] = 1
        else:
            if check[i-1] == 0:
                check[i-1] = 1
            elif check[i+1] == 0:
                check[i+1] = 1
    for i in check:
        if i == 1:
            answer += 1
    answer -= 1 # check[0] 값 제외
    return answer