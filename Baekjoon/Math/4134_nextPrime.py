def is_prime(x):
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

n = int(input())
answer = []
for i in range(n):
    num = int(input())
    while True:
        if is_prime(num):
            print(num)
            break
        else:
            num += 1
