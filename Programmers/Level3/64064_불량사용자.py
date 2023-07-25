import re
from itertools import product,combinations_with_replacement

def solution(user_id, banned_id):
    answer = set()

    results = [[] for _ in range(len(banned_id))]
    banned_id = [b.replace('*', '.') for b in banned_id]
    for i, b in enumerate(banned_id):
        for j, u in enumerate(user_id):
            if re.compile(b).fullmatch(u):
                results[i].append(j)

    # 중복 제거
    results.sort()
    stack = []
    for result in results:
        if stack and stack[-1] == result:
            stack.pop()
        else:
            stack.append(result)

    for result in list(product(*stack)):
        tmp = tuple(set(result))
        if len(tmp) == len(stack):
            answer.add(tmp)
            print(tmp)

    return len(answer)

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))