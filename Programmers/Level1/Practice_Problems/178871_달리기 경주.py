def solution(players, callings):
    answer = [None] * len(players)
    dictionary = {players[i]:i for i in range(len(players))} # [이름 : 숫자]
    for calling in callings:
        num = dictionary[calling]
        players[num], players[num-1] = players[num-1], players[num]
        dictionary[players[num]] = num
        dictionary[players[num-1]] = num-1

    for k,v in dictionary.items():
        answer[v] = k
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))