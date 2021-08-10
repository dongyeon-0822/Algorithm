import string

def transNum(n, b):
    tmp = string.digits + string.ascii_uppercase
    n, mod = divmod(n, b)
    if n == 0:
        return tmp[mod]
    else:
        return transNum(n, b) + tmp[mod]

def solution(n, t, m, p):
    answer = ''
    num=0
    while len(answer) < t*m:
        answer+=transNum(num,n)
        num += 1
    return answer[p-1:t*m:m]

solution(2,4,2,1)
