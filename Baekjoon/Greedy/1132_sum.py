# https://www.acmicpc.net/problem/1132
# 34% 실패,, 반례 찾는 중

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

# 0 이 맨 앞자리인 경우 예외처리
dic_rev = {v: k for k, v in dic.items()}
if 0 in dic_rev and dic_rev[0] in firstNum: # 0 이 맨 앞자리일 떄
    non_firstNum = list(set(dic.keys()) - set(firstNum)) # 맨 앞자리 아닌 알파벳
    non_firstNum = [[x, dic[x]] for x in non_firstNum]
    non_firstNum = sorted(non_firstNum, key=lambda x: x[1])
    dic[dic_rev[0]] = dic[non_firstNum[0][0]] # 0 이 아닌 숫자 대입

    del dic[non_firstNum[0][0]]
    dic_key = dic.keys()
    dic_value = sorted(dic.values(), reverse=True)
    dic = {k:v for k,v in zip(dic_key,dic_value)}
    dic[non_firstNum[0][0]] = 0  # 0 대입

answer = 0
for num in array:
    tmp = ""
    for n in num:
        tmp += str(dic[n])
    answer += int(tmp)
print(answer)