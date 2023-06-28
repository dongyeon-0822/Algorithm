def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k in dic:
                if dic[k] > i+1:
                    dic[k] = i+1
                else:
                    continue
            else:
                dic[k] = i+1

    for target in targets:
        result = 0
        for x in target:
            if x not in dic:
                result = -1
                break
            result += dic[x]
        answer.append(result)
    return answer

print(solution(["BC"], ["AC", "BC"]))