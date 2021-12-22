def is_groupWord(S):
    word_set = []
    pre_word = ""
    for i in S:
        if i in word_set:
            if i != pre_word:
                return False
        else:
            pre_word = i
            word_set.append(i)
    return True

N = int(input())
count = 0
for i in range(N):
    S = input()
    if is_groupWord(S):
        count+=1
print(count)