import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum_time = sum([sum(arr[:i+1]) for i in range(len(arr))])
print(sum_time)