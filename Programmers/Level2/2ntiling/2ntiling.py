def tiling(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for i in range(3,n+1):
        a, b = b, (a+b) % 1000000007
    return b
def solution(n):
    return tiling(n)