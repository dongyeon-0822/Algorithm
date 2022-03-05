import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = {input().strip() for i in range(N)}
answer = 0
for j in range(M):
    read = input().rstrip()
    if read in s:
        answer += 1
print(answer)