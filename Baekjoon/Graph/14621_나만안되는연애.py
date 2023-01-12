import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
schools = input().split()
edges = []
for _ in range(M):
    a,b,cost = map(int, input().split())
    if schools[a-1] != schools[b-1]:
        edges.append([a,b,cost])

parent = [i for i in range(N+1)]
edges.sort(key=lambda x:x[2])
result = 0
cnt = 1
for edge in edges:
    a,b,cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost
        cnt += 1
if cnt!=N:
    print(-1)
else:
    print(result)