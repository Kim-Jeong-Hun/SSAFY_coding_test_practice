# 해결법 1
# 정석적으로 10으로 나누어가면서 끝자리 더하기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def first_way(n):
    # 결과값 저장할 변수 result 선언 및 초기화
    result = 0
    
    # 숫자가 0이 될 때까지 10을 나눈 나머지를 result에 더하고 n에 n//10으로 저장
    while(n>0):
        r= n%10
        result += r
        n = n-r
        n = n//10
    return print(result)
    
first_way(T)