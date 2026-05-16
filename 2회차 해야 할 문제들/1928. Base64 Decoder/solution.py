# 비트 연산에 대한 지식이 필요하며, 매우 어려우면서도 익숙하지 않은 문제
# format() 함수, '06b'와 같이 형식 변환, 형식 지정 방법에 대한 이해가 필요
# SSAFY에서 추구하는 구현, 시뮬레이션과는 결이 맞지 않아 이해만 하고 넘어감

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
base64_table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

for i in range(1, T+1):
    answer, temp = "", ""
    C = input()
    
    for j in C:
        j = format(base64_table.index(j), '06b')
        temp += j
        
    for k in range(0, len(temp), 8):
        answer += chr(int(temp[k:k+8], 2))
            
    print(f"#{i} {answer}")