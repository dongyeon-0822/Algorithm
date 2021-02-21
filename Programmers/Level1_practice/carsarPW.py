def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
        elif 'a'<=i<='z':
            answer+=chr((ord(i)+n-97)%26+97)
        elif 'A' <= i <= 'Z':
            answer+=chr((ord(i)+n-65)%26+65)
    return answer

if __name__=='__main__':
    print(solution('AB',1))