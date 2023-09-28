import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    n = bisect_right(cards, num) - bisect_left(cards, num)
    print(n, end=" ")
