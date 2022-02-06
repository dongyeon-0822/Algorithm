def solution(id_list, report, k):
    answer = [0] * len(id_list)
    result = []
    report = list(set(report))
    cnt = [0] * len(id_list)
    for i in report:
        cnt[id_list.index(i.split()[1])] += 1
    for i, c in enumerate(cnt):
        if c >= k:
            result.append(id_list[i])
    for x in report:
        if x.split()[1] in result:
            answer[id_list.index(x.split()[0])] += 1
    return answer