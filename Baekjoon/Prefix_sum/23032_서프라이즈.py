# pypy 만 통과
import sys
input = sys.stdin.readline

N = int(input())
steak = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + steak[i - 1]

answer = [int(1e9), 0] # 차이, 무게 합
for left in range(N):
    for right in range(left + 1, N):
        total_sum = prefix_sum[right + 1] - prefix_sum[left] # 두 그룹 무게 합
        min_diff = int(1e9)

        # for mid in range(left, right):
        #     group_1 = prefix_sum[mid + 1] - prefix_sum[left]  # left ~ mid
        #     group_2 = prefix_sum[right + 1] - prefix_sum[mid + 1]  # mid+1 ~ right
        #
        #     diff = abs(group_1 - group_2)
        #     min_diff = min(min_diff, diff)

        # 이분 탐색
        low, high = left + 1, right
        while low <= high:
            mid = (low + high) // 2

            group_1 = prefix_sum[mid] - prefix_sum[left]  # left ~ mid-1
            group_2 = prefix_sum[right + 1] - prefix_sum[mid]  # mid ~ right

            diff = abs(group_1 - group_2)
            min_diff = min(min_diff, diff)

            if group_1 < group_2:
                low = mid + 1
            else:
                high = mid - 1

        if answer[0] > min_diff:
            answer = [min_diff, total_sum]
        elif answer[0] == min_diff:
            answer[1] = max(answer[1], total_sum)

print(answer[1])