import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))