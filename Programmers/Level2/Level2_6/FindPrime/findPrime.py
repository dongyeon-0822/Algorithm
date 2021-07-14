import itertools

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    s=set()
    num_list=[x for x in numbers]
    for i in range(1,len(num_list)+1):
        result=list(itertools.permutations(num_list,i))
        for j in result:
            s.add(int(''.join(j)))
    for i in s:
        if is_prime(i):
            answer+=1
    return answer

if __name__ == '__main__':
    solution("17")