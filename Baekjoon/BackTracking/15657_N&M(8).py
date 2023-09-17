# 중복 조합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# sol 1
from itertools import combinations_with_replacement
for a in combinations_with_replacement(arr, M):
    print(*a, sep=" ")

# sol 2
def backtracking(array, n):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(n, N):
        backtracking(array + [arr[i]], i)

# backtracking([], 0)