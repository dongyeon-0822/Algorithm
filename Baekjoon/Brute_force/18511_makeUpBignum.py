from itertools import product
import sys
input = sys.stdin.readline

N, K = input().split()
arr = input().split()

n = list(set([x for x in N]))
flag = True
for i in n:
    if i not in arr:
        flag = False
if flag:
    print(int(N))
else:
    N_len = len(N)
    num = [int("".join(list(x))) for x in product(arr, repeat=N_len)]
    num.append(int(N))
    num.sort()
    if num[0] != int(N):
        print(num[num.index(int(N)) - 1])
    else:
        num = []
        num = [int("".join(list(x))) for x in product(arr, repeat=N_len - 1)]
        print(max(num))
