# from bisect import bisect_right
#
# def solution(n, m, section):
#     answer = 1
#     start = section[0] - 1
#     end = start + m
#
#     while end < section[-1]:
#         idx = bisect_right(section, end)
#         start = section[idx] - 1
#         end = start + m
#         answer += 1
#
#     return answer


def solution(n, m, section):
    answer = 1
    last = section[0]
    for s in section:
        if s >= last + m:
            last = s
            answer += 1

    return answer
