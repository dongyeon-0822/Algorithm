import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

answer = 0
while len(T) >= len(S):
    if T == S:
        answer = 1
        break
    elif T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

print(answer)