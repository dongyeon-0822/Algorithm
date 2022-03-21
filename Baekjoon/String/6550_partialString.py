import sys
input = sys.stdin.readline

while True:
    try:
        s,t = input().rstrip().split()

        # sol 1 -> 반례 못 찾음
        # result = True
        # idx = 0
        # if set(s)&set(t) != set(s):
        #     result = False
        # else:
        #     for i in s:
        #         if i not in t[idx:]:
        #             result = False
        #         else:
        #             idx += t[idx:].index(i)
        # if result:
        #     print('Yes')
        # else:
        #     print('No')

        # sol 2
        result = False
        idx = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
            if idx == len(s):
                result = True
                break
        if result:
            print('Yes')
        else:
            print('No')

    except:
        break
