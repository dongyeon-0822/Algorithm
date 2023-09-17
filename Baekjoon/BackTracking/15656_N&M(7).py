# 증복 순열
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# sol 1
from itertools import product
for a in product(arr, repeat = M):
    print(*a, sep=" ")

# sol 2
def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(N):
        backtracking(array + [arr[i]])

backtracking([])