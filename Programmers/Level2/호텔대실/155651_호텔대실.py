import heapq

def solution(book_time):
    answer = 1
    book_time.sort()
    ex_end_time = []
    heapq.heappush(ex_end_time, book_time[0][1])
    for start_time, end_time in book_time[1:]:
        end_hh, end_mm = list(map(int, ex_end_time[0].split(':')))
        start_hh, start_mm = list(map(int, start_time.split(':')))
        tmp_end_time = end_hh * 60 + end_mm
        tmp_start_time = start_hh * 60 + start_mm
        if tmp_end_time + 10 > tmp_start_time:
            answer += 1
            heapq.heappush(ex_end_time, end_time)
        else:
            heapq.heappop(ex_end_time)
            heapq.heappush(ex_end_time, end_time)

    return answer

print(solution([["05:57", "06:02"], ["04:00", "06:59"], ["03:56", "07:57"], ["06:12", "08:55"], ["07:09", "07:11"]]))