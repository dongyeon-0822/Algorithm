import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

for a,b in zip(sorted(A, reverse=True),sorted(B)):
    answer += a*b
print(answer)