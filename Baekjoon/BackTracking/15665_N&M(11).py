import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr_set = sorted(set(map(int, input().split())))

def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for n in arr_set:
        backtracking(array + [n])

backtracking([])
