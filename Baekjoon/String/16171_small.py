S = input()
K = input()

kwd = ""
for i in S:
    if i.isalpha():
        kwd+=i
if K in kwd:
    print(1)
else:
    print(0)