from itertools import combinations

if __name__ =='__main__':
    n,m = map(int,input().split(' '))
    num_list = map(int,input().split(' '))
    com = list(combinations(num_list,3))
    answer = [sum(x) for x in com if sum(x)<=m]

    print(max(answer))
