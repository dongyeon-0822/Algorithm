N = input()

l = len(N)
left = sum(map(int, N[:l//2]))
right = sum(map(int, N[l//2:]))
if left == right:
    print("LUCKY")
else:
    print("READY")