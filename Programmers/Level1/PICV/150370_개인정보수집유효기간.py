def solution(today, terms, privacies):
    answer = []
    today = "".join(today.split('.'))
    terms = dict([t.split() for t in terms])
    months = [x for x in range(1,13)]

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))

        day -= 1
        if day == 0:
            day = 28
            month -= 1

        month += int(terms[term])
        plus_year, month = divmod(month, 12)
        if month == 0: year -= 1
        month = months[month-1]
        year += plus_year

        date = "".join([str(year), str(month).zfill(2),  str(day).zfill(2)])
        if date < today:
            answer.append(i+1)
    return answer
