# 콘이 셔틀을 타고 사무실로 갈 수 있는 역 도착 시각 중 제일 늦은 시각
def solution(n, t, m, timetable):
    answer = ''

    shuttle = [] # 역 도착 시간 : 09:00부터 총 n회 t분 간격
    shuttle_time = [9, 0] # [시, 분]

    for _ in range(n): # 09:00시 부터 t분 씩 더하기
        shuttle.append(tuple(shuttle_time))
        shuttle_time[1] += t
        if shuttle_time[1] >= 60:
            shuttle_time[1] -= 60
            shuttle_time[0] += 1

    timetable.sort()
    p_idx = 0
    for i, (s_h, s_m) in enumerate(shuttle): # 셔틀 버스 한대씩 옴
        cnt = 0
        while p_idx < len(timetable): # 승객 태우기
            p_h, p_m = map(int, timetable[p_idx].split(":"))
            if (p_h < s_h or (p_h == s_h and p_m <= s_m)) and cnt < m: # 시간 내에 도착했고, 인원 안 넘었는지
                cnt += 1
                p_idx += 1
            else: break
        if i == len(shuttle) - 1:  # 마지막 셔틀일 때, 태우기
            if cnt < m: # 인원이 남는다면, 셔틀 시간에
                answer = s_h, s_m
            else: # 인원이 다 찬다면, 그 전 사람 시간에
                p_h, p_m = map(int, timetable[p_idx - 1].split(":"))
                p_m -= 1
                if p_m < 0:
                    p_h -= 1
                    p_m = 59
                answer = p_h, p_m
    answer = str(answer[0]).zfill(2) + ":" + str(answer[1]).zfill(2)
    print(answer)
    return answer

solution(1, 1, 5,["08:00", "08:01", "08:02", "08:03"])
solution(2,	10,	2,	["09:10", "09:09", "08:00"])
solution(10,	60,	45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
solution(	2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
solution(	1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])