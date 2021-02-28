def gcd(a,b):
    while b>0:
        temp=b
        b=a%b
        a=temp
    return a

def solution(n, m):
    answer = []
    _gcd=gcd(n,m)
    _lcm=n*m/_gcd
    answer.append(_gcd)
    answer.append(_lcm)
    return answer