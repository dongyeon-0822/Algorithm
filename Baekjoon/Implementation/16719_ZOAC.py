import heapq
import sys
import heapq
input = sys.stdin.readline

def findMin(order, arr):
    if len(arr) == 0:
        return
    else:
        min_char = min(arr, key=lambda x:x[1])
        i = arr.index(min_char)
        order.append(min_char)
        findMin(order, arr[i+1:])
        findMin(order, arr[:i])

line = [[i,x] for i, x in enumerate(input().strip())]
orders = []
arr = []

findMin(orders, line)
for i in orders:
    arr.append(i)
    arr.sort(key=lambda x:x[0])
    tmp = list(zip(*arr))[1]
    print("".join(tmp))