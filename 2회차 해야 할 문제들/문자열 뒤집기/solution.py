# 아이디어 : 
# 문자열의 갯수가 적은 쪽이 그 문자열의 개수만큼 
# 문자열을 뒤집으면 그것이 최소 뒤집기 횟수가 된다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def flip_string():
    S = input()
    
    # S를 0인 문자열과 1인 문자열로 나누기
    s0 = list(S.split('0'))
    s1 = list(S.split('1'))
    
    # s0, s1에서 빈 문자열을 제거하고, 숫자 문자열만 카운트
    count0 = len([x for x in s0 if x != ''])
    count1 = len([x for x in s1 if x != ''])
    
    # 
    # 더 적은 쪽 출력
    return min(count0, count1)


for i in range(1, T+1):
    print(flip_string())