def nextStr(msg,i,result):
    result += msg[i]
    if result in dic:
        return i+nextStr(msg,i+1,result)
    else:
        answer.append(result[0:-1])
        dic[result] = len(dic)+1
        return 1

def solution(msg):
    global answer, dic
    answer = []
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    i = 0
    while i < len(msg):
        i = nextStr(msg,i,'')
    return answer

solution('KAKAO')