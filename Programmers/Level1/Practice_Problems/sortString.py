def solution(strings, n):
    answer = []
    strings.sort()
    return sorted(strings,key=lambda x :x[n])