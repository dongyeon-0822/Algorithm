import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
weight = []
for i, x in enumerate(arr):
    weight.append(arr[i] * (i + 1))
print(max(weight))