if __name__=='__main__':
    answer = []
    money = int(input())
    five = money//5
    for i in range(five+1):
        count = i
        if (money-i*5)%2==0:
            count += (money - i * 5) // 2
            answer.append(count)

    if len(answer)==0:
        print(-1)
    else:
        print(min(answer))
