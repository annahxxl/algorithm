def solution(N, number):
    if N == number:
        return 1
    
    answer = -1
    sets = [set() for _ in range(8)]
    
    for i in range(8):
        sets[i].add(int(str(N) * (i + 1)))
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in sets[j]:
                for op2 in sets[i - j - 1]:
                    sets[i].add(op1 + op2)
                    sets[i].add(op1 - op2)
                    sets[i].add(op1 * op2)
                    if op2 != 0:
                        sets[i].add(op1 // op2)
        
        if number in sets[i]:
            return i + 1
    
    return answer