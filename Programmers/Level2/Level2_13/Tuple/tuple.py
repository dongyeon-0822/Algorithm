def solution(s):
    answer = []
    s = [list(map(int, x.split(','))) for x in s.strip('{,}').split('},{')]
    s.sort(key=lambda x: len(x))
    for i in s:
        if len(i) == 1:
            answer.append(i[0])
        else:
            answer.append([x for x in i if x not in answer][0])
    return answer

