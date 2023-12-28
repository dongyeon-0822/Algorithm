import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(visited, start, node, arr):
    if visited[node]:
        if start == node: # 사이클 있는 경우
            # print(arr)
            return arr
        return [] # 사이클 없는 경우
    visited[node] = True # 현재 노드 방문 처리
    arr.append(node)
    return dfs(visited, start, nums[node], arr)

N = int(input())
nums = [0] + [int(input()) for _ in range(N)]

answers = []
for i in range(1, N+1):
    visit = [False] * (N + 1)
    answers.extend(dfs(visit, i, i, []))

answers = sorted(set(answers))
print(len(answers))
for x in answers:
    print(x)