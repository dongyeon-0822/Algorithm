def div(filename):
    flag = False
    head=number=tail=''
    index=0
    for i,f in enumerate(filename):
        if not f.isdigit() and flag==False:
            head += f
        elif f.isdigit():
            number += f
            flag = True
        elif not f.isdigit() and flag==True:
            index = i
            break
    if index!=0:
        tail=filename[i:]
    return [head, number, tail]

def solution(files):
    answer = []
    result = []
    for f in files:
        answer.append(div(f))

    answer.sort(key=lambda x:(x[0].lower(),int(x[1])))
    print(answer)
    return [''.join(x) for x in answer]


solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])