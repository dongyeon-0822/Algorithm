import sys
from collections import Counter

input = sys.stdin.readline

num_dic = Counter(list(input().rstrip()))

num_69 = num_dic['6'] + num_dic['9']
num_69 = num_69//2 + 1 if num_69 % 2 else num_69//2
num_dic['6'] = num_dic['9'] = num_69
answer = max(num_dic.values())
print(answer)