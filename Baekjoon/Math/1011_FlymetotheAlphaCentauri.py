import math
import sys
input = sys.stdin.readline

T = int(input())
testCase = [list(map(int, input().split())) for _ in range(T)]

for t in testCase:
    distance = t[1] - t[0]
    maxNum = math.floor(distance**(1/2))
    distance -= sum(range(maxNum))*2
    answer = math.ceil(distance/maxNum) + (maxNum-1)*2
    print(answer)