def dfs(graph, path, length):
    if len(path) == length:
        return path
    i = 0
    while graph.get(path[-1], 0) and i < len(graph[path[-1]]):
        visited, end = graph[path[-1]][i]
        if not visited:
            graph[path[-1]][i][0] = True
            result = dfs(graph, path + [end], length)
            if result : return result
            graph[path[-1]][i][0] = False
        i += 1


def solution(tickets):
    answer = []
    dic = {}
    for a, b in tickets:
        dic.setdefault(a, []).append([False,b])
    for k in dic.keys():
        dic[k].sort(key = lambda x:x[1])
    print(dic)
    answer = dfs(dic, ['ICN'], len(tickets) + 1)
    return answer

print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))
