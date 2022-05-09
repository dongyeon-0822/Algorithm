import math


def solution(s):
    answers = []
    length = range(1,math.ceil(len(s)/2) + 1)
    for l in length:
        cmp = s[:l]
        answer = l
        count = 1
        for i in range(l,len(s),l):
            if len(s) < i + l: # 남았을 때
                if count != 1:
                    answer += len(str(count))
                answer += len(s) - i
            elif i + l == len(s):
                if cmp == s[i:i+l]: # 마지막이고 같은 문자열
                    count += 1
                    answer += len(str(count))
                else: # 마지막이고 다른 문자열
                    if count != 1:
                        answer += len(str(count))
                    answer += l
            elif cmp == s[i:i+l]: # 같은 문자열
                count += 1
            else: # 다른 문자열
                if count != 1:
                    answer += len(str(count))
                answer += l
                cmp = s[i:i+l]
                count = 1
        answers.append(answer)
    return min(answers)

print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"))