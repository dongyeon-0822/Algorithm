def solution(sizes):
    w = max([max(s) for s in sizes])
    h = max([min(s) for s in sizes])
    return w*h