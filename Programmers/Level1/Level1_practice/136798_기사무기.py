import math


def numOfDivisor(n):
    num = 2
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            num+=2
    if (n**0.5)%1 == 0:
        num-=1
    return num

def solution(number, limit, power):
    divisor = []
    for n in range(1,number+1):
        x = numOfDivisor(n)
        if x > limit:
            divisor.append(power)
        else: divisor.append(x)

    return sum(divisor)
