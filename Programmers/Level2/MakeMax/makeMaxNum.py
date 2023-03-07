def solution(number, k):
    answer = ""
    length = len(number) - k
    while k > 0:
        len_k = k

        # max() 사용 시 -> 시간 초과
        max_num = number[0]
        for i in range(len_k+1):
            if number[i] == '9':
                max_num = '9'
                break
            if number[i] > max_num:
                max_num = number[i]

        idx = 0
        for i in range(len_k + 1):
            if number[i] == max_num:
                idx = i
                answer += number[i]
                break
            else:
                k -= 1
        number = number[idx+1:]
        if len(answer) == length:
            return answer
    answer += number
    return answer
