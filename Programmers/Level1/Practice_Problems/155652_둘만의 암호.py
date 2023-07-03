import string


def solution(s, skip, index):
    answer = ''

    alphabet = [x for x in list(string.ascii_lowercase) if x not in skip]
    for c in s:
        idx = (alphabet.index(c) + index)
        idx %= len(alphabet)
        answer += alphabet[idx]

    return answer