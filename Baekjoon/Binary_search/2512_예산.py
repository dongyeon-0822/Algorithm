import sys
import bisect
input = sys.stdin.readline

N = int(input())
budget = sorted(list(map(int, input().split())))
total = int(input())

total_budget = sum(budget)
max_budget = max(budget)
if total_budget <= total:
    print(max_budget)
else:
    low, high = 0, max_budget
    while low <= high:
        mid = (low + high) // 2

        sum_budget = 0
        i = bisect.bisect_left(budget, mid)
        sum_budget += sum(budget[:i])
        sum_budget += mid * (N-i)

        if sum_budget <= total:
            low = mid + 1
        else:
            high = mid - 1
    print(high)