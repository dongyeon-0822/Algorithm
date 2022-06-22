def solution(numbers):
    answer = []
    for n in numbers:
        str1 = format(n,'b')
        cnt_1 = 0
        if n%2==0: cnt_1+=1
        for i in reversed(range(len(str1))):
            if str1[i] == '0':
                break
            else:
                cnt_1 += 1
        while True:
            n=n+2**(cnt_1-1)
            str2 = format(n,'b')
            str1 = str1.zfill(len(str2))
            count = 0
            for i in range(len(str1)):
                if str1[i]!=str2[i]:
                    count +=1
            if count <= 2:
                answer.append(n)
                break
    return answer

solution([2,7])