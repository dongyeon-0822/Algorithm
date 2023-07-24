import math

def solution(k, d):
    answer = 0

    for x in range(0, d+1, k):
        answer += math.floor(math.sqrt(d*d - x*x)) // k + 1

    return answer

print(solution(2,4))