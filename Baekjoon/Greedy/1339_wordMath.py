import sys
input = sys.stdin.readline

N = int(input())
array = [input().rstrip() for _ in range(N)]

firstNum = [x[0] for x in array] # 첫번째 문자 리스트 -> 0 예외처리
max_len = max(list(map(len,array))) # 가장 긴 자리수
dic = {} # 알파벳과 숫자 dict
cnt_dic = {} # 우선순위를 정하는 dict

cnt = 9
arr = [x.zfill(max_len) for x in array] # 가장 긴 자리수에 맞추어 0 채우기
for i, col in enumerate(zip(*arr)):
    tmp = [x for x in col if x != '0' and x not in dic] # 첫번째 열부터 알파벳 추출
    for x in tmp: # 우선순위 비교하기
        if x not in cnt_dic:
            cnt_dic[x] = 10**(max_len-i) # 자리수에 따른 우선순위 부여
        else:
            cnt_dic[x] += 10**(max_len-i) # 자리수에 따른 우선순위 부여
    # sorted_dict = sorted(cnt_dic.items(), key=lambda item: item[1], reverse=True)
    # if len(sorted_dict) == 1 or (len(sorted_dict) > 1 and sorted_dict[0][1] != sorted_dict[1][1]): # 유일한 최대값인지 확인
    #     dic[sorted_dict[0][0]] = cnt
    #     cnt -= 1
    #     del cnt_dic[sorted_dict[0][0]]
sorted_dict = sorted(cnt_dic.items(), key=lambda item: item[1], reverse=True) # 남은 알파벳 dic 에 추가
for x in sorted_dict:
    dic[x[0]] = cnt
    cnt -= 1

answer = 0
for num in array:
    tmp = ""
    for n in num:
        tmp += str(dic[n])
    answer += int(tmp)
print(answer)