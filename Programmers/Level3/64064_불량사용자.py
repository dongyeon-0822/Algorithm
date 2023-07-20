import re
from itertools import product

def solution(user_id, banned_id):
    answer = set()

    results = [[] for _ in range(len(banned_id))]
    banned_id = [b.replace('*', '.') for b in banned_id]
    for i, b in enumerate(banned_id):
        for j, u in enumerate(user_id):
            if re.compile(b).fullmatch(u):
                results[i].append(j)
    
    for result in list(product(*results)):
        tmp = tuple(set(result))
        if len(tmp) == len(results):
            answer.add(tmp)

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))