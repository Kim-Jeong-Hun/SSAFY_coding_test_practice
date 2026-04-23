# N의 배수 번호인 양을 세기로 하였다.
# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 본 시점의 양 마리 수는?

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def sheep_count():
    N = int(input())
    
    # 양 최솟값
    result = 0
    # 배열은 0 ~ 9까지 10개
    flag = [0 for _ in range(10)]
    gobhagi = 1
    
    # 반복문은 flag 배열의 각 숫자가 1이 될때까지 실행되어야 함.
    # flag 배열의 원소는 10개이므로 각 원소의 총합이 10이 되면 반복문 정지
    while(sum(flag) < 10):
        # 양 세기
        sheep = N * gobhagi
        # 곱하기 크기 키워주고
        gobhagi += 1
        # 최솟값 저장
        result = sheep
        for i in str(sheep):
            flag[int(i)] = 1
    return result

for j in range(1, T+1):
    print(f"#{j} {sheep_count()}")