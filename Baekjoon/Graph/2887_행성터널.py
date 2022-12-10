import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
location = [[i]+list(map(int, input().split())) for i in range(1,N+1)]
parent = [i for i in range(N+1)]

edges = []
for p in [1,2,3]: # 각 축에 대해
    sortedLoc = sorted(location, key=lambda x:x[p])
    for i in range(N-1):
        cost = abs(sortedLoc[i][p] - sortedLoc[i + 1][p])
        edges.append((cost,sortedLoc[i][0],sortedLoc[i+1][0]))

edges.sort()

result = 0
for edge in edges:
    cost, a,b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result+=cost

print(result)