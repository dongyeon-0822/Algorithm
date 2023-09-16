# 조합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# sol 1
from itertools import combinations
for a in combinations(arr, M):
    print(*a, sep=" ")

# sol 2
def backtracking(array, n):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(n, N):
        backtracking(array + [arr[i]], i+1)

backtracking([], 0)