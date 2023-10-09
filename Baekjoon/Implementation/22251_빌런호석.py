import sys
from collections import defaultdict
from itertools import product
input = sys.stdin.readline

def count_different_bits(bin_str1, bin_str2):
    count_diff_bits = 0
    for bit1, bit2 in zip(bin_str1, bin_str2):
        if bit1 != bit2:
            count_diff_bits += 1
    return count_diff_bits

N, K, P, X = map(int, input().split())

binary_to_num = {'1110111': 0, '0010001': 1, '0111110': 2, '0111011': 3, '1011001': 4, '1101011': 5, '1101111': 6, '0110001': 7, '1111111': 8, '1111011': 9}
num_to_binary = {v:k for k,v in binary_to_num.items()}

dic = [defaultdict(list) for _ in range(10)]
for i in range(10):
    dic[i][0].append(i)
    for j in range(i+1, 10):
        n = count_different_bits(num_to_binary[i], num_to_binary[j])
        dic[i][n].append(j)
        dic[j][n].append(i)

state = str(X).zfill(K)
counts = []
for i, n in enumerate(state):
    counts.append([0] + list(dic[int(n)].keys()))

answers = []
for nums in product(*counts):
    if sum(nums) < 1 or sum(nums) > P: continue
    numbers = []
    for i, num in enumerate(nums):
        n = int(state[i])
        numbers.append(dic[n][num])
    for t in product(*numbers):
        answer = int(''.join(map(str, t)))
        if 1 <= answer <= N: answers.append(answer)
print(len(set(answers)))