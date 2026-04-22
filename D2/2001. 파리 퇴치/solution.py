# 벽을 느낀 문제
# NxN 내에서 MxM의 최댓값을 구하면 된다는 아이디어는 떠올랐지만
# 코드로 구현하지 못함
# -> 문제를 최대한 작게 분해하지 않고 크게 생각하기 때문에 코드로 구현이 안되는 것
# 같은 유형의 문제를 여러 개 풀고, 해당 유형의 문제 복습 필요


import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def max_fly_kill():
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_flies = 0
    # 2차원 배열에서 파리채 시작점이 갈 수 있는 공간만큼 순회하기
    # 파리채의 시작점이 갈 수 있는 공간은 N-M+1
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 이 공간을 순회하며 MxM 내부의 파리 수를 전부 더한 값 구하기
            # MxM 내부의 파리를 전부 더한 값을 저장하기 위한 변수 초기화
            total = 0
            for di in range(M):
                for dj in range(M):
                    total += matrix[i+di][j+dj]
            max_flies = max(max_flies, total)
            
    return max_flies

for k in range(1, T+1):
    print(f"#{k} {max_fly_kill()}")