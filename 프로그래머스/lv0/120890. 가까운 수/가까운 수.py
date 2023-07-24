def solution(array, n):
    max_diff = 100
    max_diff_idx = 100
    
    array.sort()
    
    for i in range(len(array)):
        diff = abs(array[i] - n)
        if diff < max_diff:
            max_diff = diff
            max_diff_idx = i
    
    return array[max_diff_idx]