import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(K)]
M = [list(map(int, input().split())) for _ in range(K)]

answer = []
def backtracking(n, rang, merry, cans):
    if n >= K:
        answer.append(rang + merry)
        return # 날짜가 넘어갈 때
    for j in range(N): # R 캔 하나 주기
        if cans[j] < 1: continue
        cans[j] -= 1
        for k in range(N): # M 캔 하나 주기
            if cans[k] < 1: continue
            cans[k] -= 1
            backtracking(n+1, rang + R[n][j], merry + M[n][k], cans)
            cans[k] += 1
        cans[j] += 1


day, r, m = 0, 0, 0
backtracking(day, r, m, A)
print(max(answer))