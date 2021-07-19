def solution(n):
    answer = 0
    n_one = format(n,'b').count('1')
    while True:
        n+=1
        next_one = format(n,'b').count('1')
        if next_one==n_one:
            break
    return n