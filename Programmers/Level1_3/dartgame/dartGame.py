def solution(dartResult):
    answer = [0]*3
    index=-1
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i-1]=='1':
                continue
            index += 1
            if dartResult[i+1]=='0':
                answer[index]+=10
            else:
                answer[index]+=int(dartResult[i])
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                answer[index] **= 1
            elif dartResult[i] == 'D':
                answer[index] **= 2
            elif dartResult[i] == 'T':
                answer[index] **= 3
        elif dartResult[i]=='*':
            if index>0:
                answer[index-1]*=2
            answer[index]*=2
        elif dartResult[i]=='#':
            answer[index]*=-1

    return sum(answer)

solution('1D2S#10S')