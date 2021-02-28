def GCD(a,b):
    if b == 0: return a
    else: return GCD(b, a%b)

def solution(w,h):
    gcd=GCD(w,h)
    return w*h-(w+h-gcd)