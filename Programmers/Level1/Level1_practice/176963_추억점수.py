def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    for p in photo:
        answer.append(sum([dictionary[x] for x in p if x in dictionary]))
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))