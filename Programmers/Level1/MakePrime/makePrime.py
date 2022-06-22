import math
from itertools import combinations

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1
def solution(nums):
    answer = 0
    for c in list(combinations(nums,3)):
        if isPrime(sum(c)):
            answer+=1
    return answer

if __name__=='__main__':
    solution([1,2,3,4])