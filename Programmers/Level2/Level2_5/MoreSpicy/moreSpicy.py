def solution(scoville, K):
    answer = 0
    while True:
        m=min(scoville)
        sco=0
        if m>=K: break
        else:
            answer+=1
            sco+=m
            scoville.remove(m)
            m=min(scoville)
            sco+=2*m
            scoville.remove(m)
            scoville.append(sco)

    return answer