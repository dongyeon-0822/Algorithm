import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        max_y = math.floor(math.sqrt(r2*r2 - x*x))
        min_y = math.ceil(math.sqrt(r1*r1 - x*x)) if x <= r1 else 0
        answer += max_y - min_y + 1
    return answer*4

print(solution(2,3))