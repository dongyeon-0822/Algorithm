# 순열
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# sol 1
from itertools import permutations
for a in permutations(arr, M):
    print(*a, sep=" ")

# sol 2
def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return True
    for n in arr:
        if n not in array:
            backtracking(array + [n])
backtracking([])