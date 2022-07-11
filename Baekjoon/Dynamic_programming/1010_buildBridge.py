import sys
import math
input = sys.stdin.readline

T = int(input())
testcase = [list(map(int, input().split())) for _ in range(T)]
answer = []

for t in testcase:
    n, m = t
    comb = math.factorial(m) // (math.factorial(m-n) * math.factorial(n))
    print(comb)