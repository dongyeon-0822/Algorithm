def solution(a, b):
    answer = ''
    months=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    for i in range(a-1):
        days+=months[i]
    days+=b

    if days % 7 == 0: answer = 'THU'
    elif days % 7 == 1: answer = 'FRI'
    elif days % 7 == 2: answer = 'SAT'
    elif days % 7 == 3: answer = 'SUN'
    elif days % 7 == 4: answer = 'MON'
    elif days % 7 == 5: answer = 'TUE'
    elif days % 7 == 6: answer = 'WED'

    return answer
