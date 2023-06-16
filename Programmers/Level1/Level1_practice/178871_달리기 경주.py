def solution(players, callings):
    answer = []
    dictionary = {i: players[i] for i in range(len(players))}
    for calling in callings:
        num = -1
        for k,v in dictionary:
            if v == calling:
                num = k
                break
        dictionary[k], dictionary[k-1] = dictionary[k-1], dictionary[k]

    
    return answer