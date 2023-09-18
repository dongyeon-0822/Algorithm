import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())
arr_counter = Counter(list(map(int, input().split())))
arr_set = sorted(arr_counter.keys())

def backtracking(array):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for n in arr_set:
        if arr_counter[n] != 0:
            arr_counter[n] -= 1
            backtracking(array + [n])
            arr_counter[n] += 1

backtracking([])
