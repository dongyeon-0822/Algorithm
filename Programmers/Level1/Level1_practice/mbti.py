def solution(survey, choices):
    answer = ''
    tp = ["RT", "CF", "JM", "AN"]
    score = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for x,y in zip(survey,choices):
        if y-4 < 0:
            score[x[0]] += abs(y - 4)
        else:
            score[x[1]] += abs(y - 4)
    for x in tp:
        if score[x[0]] > score[x[1]]:
            answer += x[0]
        elif score[x[0]] < score[x[1]]:
            answer += x[1]
        else:
            answer += min(x[0],x[1])
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))