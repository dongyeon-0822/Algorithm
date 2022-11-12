import sys
input = sys.stdin.readline

N = int(input())
num_arr = list(map(int, input().split()))
num_arr.sort()

M = int(input())
num = list(map(int, input().split()))

def binary_search(arr, start, end, target):
    if start > end:
        return False
    middle = (start+end) // 2
    if arr[middle] == target:
        return True
    elif arr[middle] < target:
        return binary_search(arr, middle+1, end, target)
    elif arr[middle] > target:
        return binary_search(arr, start, middle-1, target)

for n in num:
    if binary_search(num_arr, 0,len(num_arr)-1,n):
        print(1)
    else:
        print(0)
