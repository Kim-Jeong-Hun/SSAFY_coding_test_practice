# 만들 수 없는 최소 숫자를 찾는 과정을 이해하지 못함.
# 다시 풀어보기

import sys
sys.stdin = open("input.txt", "r")


def impossible_minimum():
    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    
    target = 1
    for x in coins:
        if target < x:
            break
        target += x
        
    print(target)
    
impossible_minimum()