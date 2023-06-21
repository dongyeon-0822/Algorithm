def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer+='*'
    answer+=phone_number[len(phone_number)-4:len(phone_number)]
    return answer