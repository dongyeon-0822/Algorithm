from math import gcd

def gcd_N(arr):
    n = arr[0]
    for x in arr[1:]:
        n = gcd(n, x)
    return n

def solution(arrayA, arrayB):
    gcd_a, gcd_b = gcd_N(arrayA), gcd_N(arrayB)
    max_a = gcd_b if all([a % gcd_b != 0 for a in arrayA]) else 0
    max_b = gcd_a if all([b % gcd_a != 0 for b in arrayB]) else 0
    return max(max_a, max_b)