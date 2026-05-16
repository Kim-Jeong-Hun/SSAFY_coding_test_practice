# 1. 가장 간결하고 간단한 방법 - count() 사용

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sum_char():
    str1 = list(input())
    str2 = list(input())
    result = [str2.count(c) for c in str1]
    return max(result)
    
for i in range(1, T+1):
    print(f"#{i} {sum_char()}")