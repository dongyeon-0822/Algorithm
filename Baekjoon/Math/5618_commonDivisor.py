from math import gcd

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    result = num[0]
    for i in range(1, len(num)):
        result = gcd(result, num[i])
    answer = []
    for i in range(1, int(result**0.5)+1):
        if result % i == 0:
            answer.append(i)
            if i != result//i:
                answer.append(result//i)
    answer.sort()
    for i in answer:
        print(i)
