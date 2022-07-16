import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
K = int(input())
card = [int(input()) for _ in range(N)]

num = []
comb = list(permutations(card, K))
for c in comb:
    n = ''.join(map(str, c))
    num.append(n)
print(len(set(num)))