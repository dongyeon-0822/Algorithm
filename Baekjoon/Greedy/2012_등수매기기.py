import sys
input = sys.stdin.readline

N = int(input())
expected = [int(input()) for _ in range(N)]
expected.sort()

answer = 0
for i in range(N):
    answer += abs(expected[i] - (i+1))
print(answer)
