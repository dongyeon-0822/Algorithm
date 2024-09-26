# 풀이 예정 
import math


def find_original_sequence(partial_sums):
    n = int(math.log2(len(partial_sums)))
    a = [0] * n  # 원래 수열 초기화

    for i in range(1, 2 ** n):
        curr_sum = 0
        for j in range(n):
            if i & (1 << j):
                curr_sum += a[j]
        if curr_sum in partial_sums:
            partial_sums.remove(curr_sum)
            for j in range(n):
                if i & (1 << j):
                    a[j] = 1
    return a

n = int(input())
partial_sums = list(map(int, input().split()))
original_sequence = find_original_sequence(partial_sums)
print(original_sequence)
