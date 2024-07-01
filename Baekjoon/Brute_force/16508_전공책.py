import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline

answer = []
T = input().rstrip()
N = int(input())
t_dic = Counter(T)
books_dic = {}
for i in range(N):
    price, name = input().split()
    name_counter = Counter(name)
    alpha = set(t_dic.keys()) & set(name_counter.keys())
    book_dic = {a: name_counter[a] for a in alpha}
    books_dic[i] = [price, book_dic]
for i in range(1, N + 1):
    for comb in combinations(books_dic.keys(), i):
        tmp_price = 0
        tmp_dic = Counter({k: 0 for k in t_dic.keys()})
        for c in comb:
            tmp_price += int(books_dic[c][0])
            tmp_dic += Counter(books_dic[c][1])
        for k in t_dic.keys():
            if tmp_dic[k] < t_dic[k]: break
        else:
            answer.append(tmp_price)

if answer:
    print(min(answer))
else:
    print(-1)
