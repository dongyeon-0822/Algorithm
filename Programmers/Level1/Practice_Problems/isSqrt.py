def solution(n):
    answer = 0
    n_sqrt=n**0.5
    if int(n_sqrt)==n_sqrt:
        return (n_sqrt+1)**2
    else: return -1
    return answer
