S = input().rstrip()

if len(S) == 0:
    print(0)
    exit()
if S.isdigit():
    print(len(S))
    exit()

def unzip(zip_str):
    buffer = ""
    for i, s in enumerate(zip_str):
        if s == '(':
            n = 0 if len(buffer) - 1 < 0 else len(buffer) - 1
            k = int(buffer[-1])
            return n + k * unzip(zip_str[i + 1:])
        elif s == ')':
            return len(buffer)
        else:
            buffer += s

print(unzip(S))