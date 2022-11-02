import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    if n in cards:
        print(1,end=" ")
    else:
        print(0,end=" ")