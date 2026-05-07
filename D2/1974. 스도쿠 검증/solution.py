import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 가로 검사
# 1부터 9까지 중복이 있으면 안됨
def horizontal_check(matrix):
    for i in range(9):
        new_arr = sorted(matrix[i])
        for j in range(len(new_arr)):
            if new_arr[j] != j + 1:
                return 0
    return 1

# 세로 검사
def vertical_check(matrix):
    for i in range(9):
        # 원래 2차원배열 matrix에서 각 행의 열들을 모아서 하나의 행으로 만들기
        new_arr = [matrix[x][i] for x in range(len(matrix))]
        sorted_arr = sorted(new_arr)
        for j in range(len(sorted_arr)):
            if sorted_arr[j] != j+1:
                return 0
    return 1

# 3x3 격자 검사
def matrix_check(matrix):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            new_arr = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    new_arr.append(matrix[k][l])
            sorted_arr = sorted(new_arr)
            for a in range(9):
                if sorted_arr[a] != a+1:
                    return 0
    return 1

for t in range(1, T+1):
    answer = 0
    matrix = []
    for _ in range(9):
        matrix.append(list(map(int, input().split())))

    # 3개의 검사 모두 통과 시 스도쿠 퍼즐 인정
    if horizontal_check(matrix) == 1 and vertical_check(matrix) == 1 and matrix_check(matrix) == 1:
        answer = 1
    else:
        answer = 0

    print(f"#{t} {answer}")