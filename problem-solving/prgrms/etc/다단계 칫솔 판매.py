def calculate(name, price):
    global member_dic

    tax = int(price * 0.1)
    remain = price - tax

    if int(price * 0.1) < 1:
        member_dic[name][1] += price
        return

    member_dic[name][1] += remain
    up_name = member_dic[name][0]
    
    if up_name == '':
        return
    
    calculate(up_name, tax)

def solution(enroll, referral, seller, amount):
    global member_dic

    member_dic = {} # 멤버 이름: [추천인, 이익금]

    for e, r in zip(enroll, referral):
        member_dic[e] = ['', 0]
        if r != '-':
            member_dic[e][0] = r

    for s, a in zip(seller, amount):
        price = a * 100
        calculate(s, price)

    answer = []

    for value in member_dic.values():
        answer.append(value[1])

    return answer