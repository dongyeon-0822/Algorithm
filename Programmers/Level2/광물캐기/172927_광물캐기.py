def solution(picks, minerals):
    answer = 0
    fatigue = {"diamond" : [1,5,25], "iron" : [1,1,5], "stone" : [1,1,1]}

    weight = []
    tmp = [0] * 3
    cnt = 0
    for mineral in minerals:

        dia, iron, stone = fatigue[mineral]
        tmp[0] += dia
        tmp[1] += iron
        tmp[2] += stone

        cnt += 1
        if cnt % 5 == 0 or cnt == len(minerals):
            weight.append(tmp)
            tmp = [0] * 3
        if cnt >= sum(picks) * 5: break

    weight.sort(key=lambda x:(-x[2], -x[1]))
    idx = 0
    for i, pick in enumerate(picks):
        if pick == 0: continue # 곡괭이 없는 경우
        if len(weight) - idx <= 0: break # 남은 광물이 없는 경우

        if pick <= len(weight) - idx:
            answer += sum(list(zip(*weight[idx:idx+pick]))[i])
            idx += pick
        else:
            answer += sum(list(zip(*weight[idx:len(weight)]))[i])
            idx += pick

    return answer

print(solution(	[0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))