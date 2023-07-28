import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = sorted(list(input().split()))

for c in list(combinations(alpha, L)):
    v = len(set(c) & set(['a', 'e', 'i', 'o', 'u']))
    if v >= 1 and L - v >= 2:
        print("".join(c))


