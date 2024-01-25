# pypy 통과, python 시간초과
import sys
input = sys.stdin.readline

A, B = input().strip(), input().strip()
answer = [["" for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            answer[i][j] = answer[i-1][j-1] + A[i-1]
        else:
            if len(answer[i-1][j]) > len(answer[i][j-1]):
                answer[i][j] = answer[i-1][j]
            else:
                answer[i][j] = answer[i][j-1]
print(len(answer[len(A)][len(B)]))
print(answer[len(A)][len(B)])