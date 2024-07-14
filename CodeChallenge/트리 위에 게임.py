# 테스트 케이스 20/100
import sys
sys.setrecursionlimit(100000)


N = int(input())
score = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
depth = [-1] * (N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프의 depth 구하기
def dfs(node, d):
    depth[node] = d
    for child in graph[node]:
        if depth[child] == -1:
            dfs(child, d+1)
dfs(1, 0)

for i in range(1, N+1):
    if len(graph[i]) == 1 and i != 1:
        tmp_score = [0,0]
        node = i
        tmp_score = tmp_score[1] + node, tmp_score[0]
        score[node].append(tmp_score)
        while True:
            flag = False
            for n in graph[node]:
                if depth[n] < depth[node]:
                    node = n
                    flag = True
                    break
            if not flag: break
            # node = graph[node][0]
            tmp_score = tmp_score[1] + node, tmp_score[0]
            score[node].append(tmp_score)

for i in range(1, N+1):
    for a, b in score[i]:
        if a >= b:
            print(1)
            break
    else:
        print(0)

