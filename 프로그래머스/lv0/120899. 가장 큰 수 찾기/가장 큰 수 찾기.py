def solution(array):
    idx = 0
    num = array[idx]
    
    for i in range(len(array)):
        if num < array[i]:
            idx = i
            num = array[i]
            
    return [num, idx]