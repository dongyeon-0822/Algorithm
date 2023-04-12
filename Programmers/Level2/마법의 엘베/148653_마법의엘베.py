def solution(storey):
    answer = 0

    while storey:
        storey, mod = divmod(storey, 10)
        if mod > 5 or mod == 5 and storey%10 >= 5:
            answer += 10 - mod
            storey += 1
        else:
            answer += mod

    return answer

print(solution(555))

def solution_2(n):
    if n < 10:
        return min(n, 11-n)
    n, mod = divmod(n, 10)
    return min(mod + solution(n), 10 - mod + solution(n+1))

print(solution(555))