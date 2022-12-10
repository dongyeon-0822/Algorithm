import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x: # 루트 노드를 찾을 때까지
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

v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a,b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort() # 비용 순으로 정렬
max_edge = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        max_edge = cost

print(result - max_edge)