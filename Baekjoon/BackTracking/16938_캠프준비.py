import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
answer = 0

# 조합
def backtracking(arr, n):
    global answer

    if len(arr) >= 2:
        if L <= sum(arr) <= R and arr[-1] - arr[0] >= X:
            answer += 1
    if len(arr) == N: return True
    for i in range(n, N):
        backtracking(arr + [A[i]], i + 1)

backtracking([], 0)
print(answer)

