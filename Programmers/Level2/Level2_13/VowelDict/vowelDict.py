def solution(word):
    answer = 0
    word = word.replace('A','1').replace('E','2').replace('I','3').replace('O','4').replace('U','5')
    word+='0'*(5-len(word))

    for i,w in enumerate(word):
        if w=='0': continue
        if i==0:
            answer+=(int(w)-1)*sum([5**s for s in range(5)])
        else:
            answer+=(int(w)-1)*sum([5**s for s in range(5-i)])+1

    return answer+1

solution('EIO')