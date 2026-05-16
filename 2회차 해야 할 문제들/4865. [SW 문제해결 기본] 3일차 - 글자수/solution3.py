# 3. 직접 구현(완전 탐색) 방법

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sum_char():
    str1 = list(input())
    str2 = list(input())
    result = [0 for _ in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                result[i] += 1
    return max(result)

for k in range(1, T+1):
    print(f"#{k} {sum_char()}")