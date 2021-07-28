def solution(n):
    a,b = 0,1
    if n<2:
        return n
    else:
        for i in range(2,n+1):
            a,b = b%1234567,(a+b)%1234567
        return b%1234567