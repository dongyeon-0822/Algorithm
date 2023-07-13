import re

def solution(user_id, banned_id):
    answer = 0

    results = [[] for _ in range(len(banned_id))]
    banned_id = [b.replace('*', '.') for b in banned_id]
    for i, b in enumerate(banned_id):
        for j, u in enumerate(user_id):
            if re.compile(b).fullmatch(u):
                results[i].append(j)

    tmp = []
    for i, result in enumerate(results):
        for j, x in enumerate(result):
            if x in tmp: continue
            else:
                tmp.append(x)
                break
        else:
            if len(tmp) != i+1:
                break
        if len(tmp) == len(results):
            answer += 1
            tmp = []

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))