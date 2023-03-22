def solution(food):
    answer = '0'
    food = [(i,x) for i,x in enumerate(food)]
    for i,x in food[::-1]:
        tmp = str(i) * (x//2)
        answer = tmp + answer + tmp
    return answer