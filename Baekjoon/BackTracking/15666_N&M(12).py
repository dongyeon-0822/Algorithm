import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr_set = sorted(set(map(int, input().split())))

def backtracking(array, n):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(n, len(arr_set)):
        backtracking(array + [arr_set[i]], i)

backtracking([], 0)
