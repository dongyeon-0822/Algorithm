from collections import deque
def solution(tickets):
    answer = []
    dic = {}
    for a, b in tickets:
        dic.setdefault(a, []).append(b)

    q = deque()
    node = 'ICN'
    q.append(node)

    while tickets:
        x = q.popleft()
        for n_node in dic[x]:
            q.append(n_node)

        answer.append(node)
        while n_node := dic.get(node):
            answer.append(n_node[0])
            node = dic[node].pop(0)
        return answer

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
