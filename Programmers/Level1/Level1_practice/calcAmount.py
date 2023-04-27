def solution(price, money, count):
    n = sum([price*(i+1) for i in range(count)])
    return max(0,n-money)