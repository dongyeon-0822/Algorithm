def solution(players, callings):
    answer = []
    dictionary = {i: players[i] for i in range(len(players))}
    for calling in callings:
        num = -1
        for k,v in dictionary.items():
            if v == calling:
                num = k
                break
        dictionary[k], dictionary[k-1] = dictionary[k-1], dictionary[k]

    for i in range(len(players)):
        answer.append(dictionary[i])
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))