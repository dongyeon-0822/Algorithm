import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]

answer = 1
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] != 0 and 0 not in [arr[i-1][j-1], arr[i-1][j], arr[i][j-1]]:
            arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1
            answer = max(answer, arr[i][j])

if sum([sum(a) for a in arr]) == 0: # 모두 0일 때 예외 처리
    answer = 0
print(answer**2)