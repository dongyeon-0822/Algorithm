import sys
input = sys.stdin.readline

N, M = map(int, input().split())
fighting_dic = {}
for _ in range(N):
    name, value = input().split()
    if int(value) not in fighting_dic:
        fighting_dic[int(value)] = name
fighting_arr = list(fighting_dic.keys())

def binary_search(num):
    s, e = 0, len(fighting_arr) - 1
    while s <= e:
        m = (s + e) // 2
        if fighting_arr[m] >= num:
            e = m - 1
        else:
            s = m + 1

    return fighting_dic[fighting_arr[e + 1]]

for _ in range(M):
    n = int(input())
    bound = binary_search(n)
    print(bound)
