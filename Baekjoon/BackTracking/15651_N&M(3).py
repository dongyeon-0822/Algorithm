# 중복 순열
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# sol 1
from itertools import product
for arr in list(product(list(range(1,N+1)), repeat = M)):
    print(*arr, sep=" ")

# sol 2
def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for n in range(1, N+1):
        backtracking(array + [n])

backtracking([])