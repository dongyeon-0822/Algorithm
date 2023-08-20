def solution(targets):
    answer = 0

    targets = sorted(targets)
    bound = -1
    for s,e in targets:
        if s >= bound:
            bound = e
            answer += 1
        else:
            bound = min(bound, e)
    return answer

