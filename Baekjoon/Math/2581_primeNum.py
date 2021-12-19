import math


def is_prime(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    M = int(input())
    N = int(input())
    primeNum = []
    for i in range(M,N+1):
        if is_prime(i):
            primeNum.append(i)
    if len(primeNum)==0:
        print(-1)
    else:
        print(sum(primeNum))
        print(min(primeNum))