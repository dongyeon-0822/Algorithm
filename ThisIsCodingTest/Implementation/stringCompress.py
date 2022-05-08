def solution(s):
    answers = []
    length = range(1,len(s)//2)
    for l in length:
        cmp = s[:l]
        answer = l
        count = 0
        for i in range(0,len(s),l):
            if len(s) < i + l: # 마지막 남았을 때
                answer += len(s) - i
            elif cmp == s[i:i+l]: # 같은 문자열
                count += 1
                if i + l == len(s) and count >= 1:
                    answer += 1
            else: # 다른 문자열
                if count >= 1:
                    answer += 1
                answer += l
                cmp = s[i:i+l]
                count = 0
        answers.append(answer)
    return min(answers)

print(solution("ababcdcdababcdcd"))