# 해결법 2
# 입력을 문자열로 받은 후, 
# 잘라서 배열에 저장
# 숫자로 바꾸면서 하나씩 더하기

import sys
sys.stdin = open("input.txt", "r")

# 입력을 문자열로 받아오기 int() 사용x
T = input()

def second_way(n):
    # 결과값 저장용 변수 result 선언 및 초기화
    result = 0
    
    # 문자열로 받아온 입력값 잘라서 리스트 arr에 저장
    arr = list(n)
    
    # 반복하며 정수형으로 바꿔가며 더하기
    for i in range(len(arr)):
        result += int(arr[i])
    
    return print(result)

second_way(T)