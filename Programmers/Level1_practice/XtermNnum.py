def solution(x, n):
    if x==0: return [0]*n
    answer = list(range(x,x*(n+1),x))
    return answer