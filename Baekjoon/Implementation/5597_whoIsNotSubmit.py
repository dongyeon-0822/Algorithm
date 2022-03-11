import sys
input = sys.stdin.readline

check = [0]*30
for i in range(28):
    check[int(input()) - 1] = 1
for i, c in enumerate(check):
    if c == 0:
        print(i+1)