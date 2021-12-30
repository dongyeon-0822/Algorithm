def is_right(s):
    if s[0] not in ['A','B','C','D','E','F']:
        return False
    if 'A' not in s[1:]:
        return False
    if 'F' not in s[1:]:
        return False
    if 'C' not in s[1:]:
        return False

s = input()
