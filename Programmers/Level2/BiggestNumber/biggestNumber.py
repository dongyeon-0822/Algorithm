from functools import cmp_to_key
def compare(a,b):
    if int(a+b) >= int(b+a):
        return -1
    else:
        return 1
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = str(int(''.join(numbers)))
    return answer