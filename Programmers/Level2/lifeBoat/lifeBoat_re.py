def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    h, l = 0, len(people) - 1
    while h <= l:
        if people[h] + people[l] <= limit:
            h += 1
            l -= 1
        else:
            h += 1
        answer += 1
    return answer