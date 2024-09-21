import sys, math
input = sys.stdin.readline

x, y, c = map(float, input().split())

def find_width(d):
    h1 = math.sqrt(x**2 - d**2)
    h2 = math.sqrt(y**2 - d**2)
    return (h1 * h2) / (h1 + h2)

low, high = 0, min(x, y)
while high - low > 1e-5:
    mid = (low + high) / 2
    if find_width(mid) > c:
        low = mid
    else:
        high = mid

print(f"{low:.3f}")