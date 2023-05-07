def is_continuous(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def solution(babbling):
    answer = 0
    can_babbling = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for i,x in enumerate(can_babbling):
            b = b.replace(x, str(i))
        if b.isdigit() and not is_continuous(b):
            answer += 1
    return answer