# 2. collections 모듈의 Counter 객체 사용 - 표준 라이브러리 사용법

import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

T = int(input())

def sum_char():
    str1 = list(input())
    str2 = input()
    counter = Counter(str2)
    result = counter.most_common(len(str2))
    # result 배열의 길이만큼 비교
    # 만약 result에 저장된 해당 문자가 str1에 있으면 바로 리턴 (최빈값 순서대로)
    for i in range(len(result)):
        if(result[i][0] in str1):
            return result[i][1]
    
for j in range(1, T+1):
    print(f"#{i} {sum_char()}")