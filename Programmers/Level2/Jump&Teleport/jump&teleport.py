def solution(n):
    # sol1
    return bin(n).count('1')
    # sol2
    ans = 0
    while n:
        ans += n % 2
        n //= 2
    return ans