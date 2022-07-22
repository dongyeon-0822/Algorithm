# 풀이 참고
# S -> T는 시간초과가 난다. T -> S로 풀이해야 한다.
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def DFS(t):
    if len(t) == len(S):
        return t == S
    if t[-1] == 'A'and DFS(t[:-1]):
        return True
    if t[0] == 'B'and DFS(t[:0:-1]):
        return True

print(1 if DFS(T) else 0)