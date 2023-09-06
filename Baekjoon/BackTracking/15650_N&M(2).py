# 조합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# sol 1
from itertools import combinations
for arr in list(combinations(list(range(1,N+1)), M)):
    print(*arr, sep=" ")

# sol 2
def backtracking(array, n):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(n, N+1):
        if i not in array:
            backtracking(array + [i], i)

backtracking([], 1)