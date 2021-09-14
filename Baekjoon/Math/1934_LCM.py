def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
if __name__=='__main__':
    answer = []
    T = int(input())
    for i in range(T):
        A,B = list(map(int,input().split()))
        answer.append(lcm(A,B))
    for a in answer:
        print(a)