# 다른 답을 참고하고 품
import bisect

def solution(info, query):
    answer = []
    # 모든 경우의 수를 info_list 에 넣어준다
    info_list = {}
    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_list[lang + job + career + food] = []
    # info 를 돌면서 나올 수 있는 모든 경우를 추가해준다.
    for i in info:
        tmp = i.split()
        for lang in [tmp[0], "-"]:
            for job in [tmp[1], "-"]:
                for career in [tmp[2], "-"]:
                    for food in [tmp[3], "-"]:
                        info_list[lang + job + career + food].append(int(tmp[4]))

    # 각 list 별로 점수들을 정렬해준다.
    for key in info_list.keys():
        info_list[key].sort()

    for q in query:
        q = q.replace(" and ", "").split() # query 와 점수로 나눈다.
        scores = info_list[q[0]]
        score = int(q[1])
        # 이진 탐색
        idx = bisect.bisect_left(scores, score)
        answer.append(len(scores) - idx)
    return answer