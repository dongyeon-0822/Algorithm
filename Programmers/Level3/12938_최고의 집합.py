def solution(n, s):
    answer = []

    if s // n == 0:
        return [-1]
    else:
        answer = [s // n] * n
        r = s % n
        for i in range(n - 1, n - r - 1, -1):
            answer[i] += 1

    return answer
