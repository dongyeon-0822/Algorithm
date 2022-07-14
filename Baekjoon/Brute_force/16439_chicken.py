import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
prefer = [list(map(int, input().split())) for _ in range(N)]

answer = []
comb = combinations(list(range(M)), 3)
for c in comb:
    tmp = 0
    for p in prefer:
        tmp += max(p[c[0]], p[c[1]], p[c[2]])
    answer.append(tmp)
print(max(answer))