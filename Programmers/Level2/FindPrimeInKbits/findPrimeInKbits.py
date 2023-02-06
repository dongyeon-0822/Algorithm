import math
import string

# 진법 변환 함수
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    k_bit = convert(n,k)
    nums = []
    for num in k_bit.split('0'):
        if num != "" and is_prime_number(int(num)):
            nums.append(num)
    return len(nums)

solution(437674, 3)