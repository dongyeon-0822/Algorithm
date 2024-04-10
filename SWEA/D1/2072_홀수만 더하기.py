T = int(input())

for t in range(1, T + 1):
    answer = 0
    for n in list(map(int, input().split())):
        if n % 2 == 1:
            answer += n
    print('#' + str(t), answer)