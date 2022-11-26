# 이코테 크루스칼 알고리즘
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input()) # 노드 수
M = int(input()) # 간선 수
edges = []
for _ in range(M):
    a,b, cost = map(int,input().split())
    edges.append((cost,a,b))
parent = [i for i in range(N+1)]
result = 0

edges.sort() # 비용 순으로 정렬

for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)