# 숫자 배열 회전
# 각 회전 모양을 보니까 숫자 채우는 방식의 차이
# 270도 배열이랑, 마지막 join에서 map(str, array90) 못 함.
# 그냥 떠올리지도 못함.
# 무조건 다시 풀기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    # 배열 입력 받기
    matrix = []
    for _  in range(N):
        array = list(map(int, input().split()))
        matrix.append(array)
        
    # 입력용 카운트, 리스트
    count = 0
    input_list = []
    
    for i in range(N):
        for j in range(N):
            input_list.append(matrix[i][j])
    
    array90 = [[0]*N for _ in range(N)]
    array180 = [[0]*N for _ in range(N)]
    array270 = [[0]*N for _ in range(N)]
    
    # array90
    for j in range(N-1, -1, -1):
        for i in range(N):
            array90[i][j] = input_list[count]
            count += 1
            
    
    # array180
    count = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            array180[i][j] = input_list[count]
            count += 1
    
    # array270
    count = 0
    for j in range(N):
        for i in range(N-1, -1, -1):
            array270[i][j] = input_list[count]
            count += 1
    
    print(f"#{t}")
    
    for i in range(N):
        print("".join(map(str, array90[i])), end = ' ')
        print("".join(map(str, array180[i])), end = ' ')
        print("".join(map(str, array270[i])))