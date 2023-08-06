from collections import defaultdict
import math

def sub_time(before, after):
    before_hh, before_mm = map(int, before.split(':'))
    after_hh, after_mm = map(int, after.split(':'))
    return (after_hh - before_hh) * 60 + (after_mm - before_mm)

def solution(fees, records):
    answer = []

    record_dic = defaultdict(list) # {'car_num' : [sum_time, time, in_out]}
    base_time, base_fee, unit_time, unit_fee = fees
    for record in records:
        time, car_num, in_out = record.split()
        if record_dic[car_num]:
            sum_time, prev_time, prev_in_out = record_dic[car_num]
            if prev_in_out == 'IN':
                sum_time += sub_time(prev_time, time)
                record_dic[car_num] = [sum_time, time, in_out]
            else:
                record_dic[car_num] = [sum_time, time, in_out]
        else:
            record_dic[car_num] = [0, time, in_out]

    for k, v in record_dic.items():
        if v[2] == 'IN':
            v[0] += sub_time(v[1], '23:59')
    print(record_dic)

    for k, v in sorted(record_dic.items()):
        fee = base_fee + math.ceil((v[0] - base_time) / unit_time) * unit_fee if v[0] - base_time > 0 else base_fee
        answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))