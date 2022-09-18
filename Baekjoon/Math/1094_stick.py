import sys
input = sys.stdin.readline

X = int(input())
stick = [64]

while sum(stick) > X:
    half = stick.pop() // 2
    stick.append(half)
    stick.append(half)
    if sum(stick[:-1]) >= X:
        stick.pop()

print(len(stick))

