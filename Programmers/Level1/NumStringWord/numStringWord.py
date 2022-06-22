def solution(s):
    numString = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for i in list(numString.keys()):
        index = s.find(i)
        while index != -1:
            sl= list(s)
            nl= list(numString[i])
            sl[index:index+len(i)]=nl
            s=''.join(sl)
            index = s.find(i)
    return int(s)

if __name__ =='__main__':
    solution("23four5six7")