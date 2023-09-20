import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())
arr_counter = Counter(list(map(int, input().split())))
arr_set = sorted(arr_counter.keys())

def backtracking(array, n):
    if len(array) == M:
        print(*array, sep=" ")
        return
    for i in range(n, len(arr_set)):
        if arr_counter[arr_set[i]] != 0:
            arr_counter[arr_set[i]] -= 1
            backtracking(array + [arr_set[i]], i)
            arr_counter[arr_set[i]] += 1

backtracking([], 0)
