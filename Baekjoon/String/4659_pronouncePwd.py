import sys
input = sys.stdin.readline

def is_pronounced(s):
    vowel = ['a','e','i','o','u']

    if len(set(vowel) & set(s)) == 0: # 모음을 반드시 하나 포함 하는지
        return False

    first = s[0]
    flag = False # 모음이면 True, 자음이면 False
    if first in vowel:
        flag = True
    count = 1
    for i in range(1,len(s)):
        if s[i] in vowel and flag: # 모음 연속이면
            count += 1
        elif s[i] in vowel and not flag: # 자음->모음이면
            count = 1
            flag = True
        elif s[i] not in vowel and not flag: # 자음 연속이면
            count += 1
        elif s[i] not in vowel and flag: # 자음 -> 모음이면
            count = 1
            flag = False
        if count >= 3:
            return False
        if s[i - 1] == s[i] and s[i] != 'e' and s[i] != 'o':
            return False
    return True


while True:
    S = input().strip()
    if S == 'end':
        break
    if is_pronounced(S):
        print("<"+ S +">" + " is acceptable.")
    else:
        print("<"+ S +">" + " is not acceptable.")