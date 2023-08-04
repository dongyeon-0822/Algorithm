from itertools import product

def calculate_grade(ryan, apeach):
    ryan_grade = 0
    apeach_grade = 0
    for i, (x, y) in enumerate(zip(ryan, apeach)):
        if x == y == 0: continue
        if x > y : ryan_grade += i
        else: apeach_grade += i
    return ryan_grade - apeach_grade

def solution(n, info):
    answer = [-1]
    info = info[::-1]

    max_grade = 0
    for result in list(product([1,0], repeat = 11)): # 모든 승패의 경우의 수
        Ryan = [info[i] + 1 if x else 0 for i, x in enumerate(list(result))]
        if n >= sum(Ryan):
            sub_grade = calculate_grade(Ryan, info)
            if sub_grade > max_grade:
                answer = Ryan[::-1]
                max_grade = sub_grade
                answer[-1] += n - sum(Ryan) # 남은 화살은 0점에
    return answer

solution(5,[2,1,1,1,0,0,0,0,0,0,0])