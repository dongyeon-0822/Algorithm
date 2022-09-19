def solution(n, left, right):
    answer = []
    for v in range(left, right+1):
        r = v//n
        c = v%n
        answer.append(max(r,c)+1)
    return answer
print(solution(4,7,14))     