import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
for x in permutations(range(1, N+1)):
    print(*x)