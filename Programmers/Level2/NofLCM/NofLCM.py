from math import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

def solution(arr):
    answer = 0
    a = arr[0]
    for i in range(1,len(arr)):
        a = int(lcm(a,arr[i]))
    return a

print(solution([2,6,8,14]))