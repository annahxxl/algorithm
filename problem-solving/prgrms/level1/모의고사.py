def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0
    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            s1 += 1
        if p2[i % 8] == answers[i]:
            s2 += 1
        if p3[i % 10] == answers[i]:
            s3 += 1
    winner_score = max(s1, s2, s3)
    if s1 == winner_score:
        answer.append(1)
    if s2 == winner_score:
        answer.append(2)
    if s3 == winner_score:
        answer.append(3)
    answer.sort()
    return answer
# enumerate 사용하여 답안을 작성하면 코드가 더 간결해질 수 있다.