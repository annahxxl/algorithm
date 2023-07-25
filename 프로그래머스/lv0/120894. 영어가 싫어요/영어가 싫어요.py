def solution(numbers):
    answer = ''
    dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    key = ''

    for s in numbers:
        key += s
        if key in dic:
            answer += dic[key]
            key = ''
    
    return int(answer)