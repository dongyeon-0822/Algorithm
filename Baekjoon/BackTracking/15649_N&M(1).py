# 순열
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# sol 1
from itertools import permutations
for arr in list(permutations(list(range(1,N+1)), M)):
    print(*arr, sep=" ")

# sol 2
def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for n in range(1, N+1):
        if n not in array:
            backtracking(array + [n])
backtracking([])