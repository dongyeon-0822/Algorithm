def solution(n):
    # sol1
    return bin(n).count(1)
    # sol2
    ans = 0
    while n>0:
        if n%2:
            n-=1
            ans+=1
        n//=2
    return ans

