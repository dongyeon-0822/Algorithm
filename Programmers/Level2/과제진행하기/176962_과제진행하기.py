def past_time(time, playtime):
    hh, mm = map(int, time.split(':'))
    div, mod = divmod(mm + playtime, 60)
    hh += div
    mm = mod
    hh = str(hh).zfill(2)
    mm = str(mm).zfill(2)
    return hh + ':' + mm

def sub_time(before, after):
    before_hh, before_mm = map(int, before.split(':'))
    after_hh, after_mm = map(int, after.split(':'))
    return (after_hh - before_hh) * 60 + (after_mm - before_mm)

def solution(plans):
    answer = []

    plans = sorted(plans, key=lambda x: x[1])
    stack = []
    idx = 0
    while stack or idx < len(plans):
        if len(stack) == 0: # 현재 진행 중인 plan 없는 경우
            name, start, playtime = plans[idx]
            stack = [[name, playtime]]
            idx += 1

        name, playtime = stack.pop()
        if idx < len(plans):
            _name, _start, _playtime = plans[idx]
        else:
            _start = '99:99'

        end = past_time(start, int(playtime))
        if end > _start: # 새로운 과제 시작
            stack.append([name, sub_time(_start, end)])
            stack.append([_name, _playtime])
            start = _start
            idx += 1
        elif end < _start: # 진행 중인 과제 종료
            answer.append(name)
            start = end
        else: # 과제 종료 및 새로운 과제 시작
            answer.append(name)
            stack.append([_name, _playtime])
            start = _start
            idx += 1

    return answer

print(solution([['A', "12:00", "30"], ['B', "12:10", "20"], ['C', "15:00", "40"], ['D', "15:10", "30"]]))