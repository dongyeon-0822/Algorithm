from collections import Counter

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: parent[a] = b
    else: parent[b] = a

def solution(cards):
    parent = [x for x in range(len(cards)+1)]
    for i, card in enumerate(cards):
        union_parent(parent, i+1, card)

    root_list = [find_parent(parent, x) for x in parent[1:]]
    counter = Counter(root_list).most_common(2)
    if len(counter) == 1:
        return 0
    else:
        return counter[0][1] * counter[1][1]

print(solution([7, 2, 4, 5, 6, 1, 3]))