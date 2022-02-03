def isPrime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        i = 2
        while i <= n / i:
            if n % i == 0:
                return 0
            i += 1
        return 1
N = int(input())
arr = list(map(int,(input().split())))
cnt = 0
for a in arr:
    if isPrime(a):
        cnt += 1
print(cnt)