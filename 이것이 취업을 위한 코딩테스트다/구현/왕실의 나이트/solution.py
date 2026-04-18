# 복습 필요

import sys
sys.stdin = open("input.txt", "r")

# 좌표를 입력으로 받기
point = input()

# 가능한 경우의 수 저장하는 변수
COUNT = 0

# 나이트가 이동 가능한 8개 방향을 행 이동과 열 이동으로 나누어 배열로 저장
# 좌1상2, 우1상2, 좌2상1, 좌2하1, 우2상1, 우2하1, 좌1하2, 우1하2
column_moves = [-1, 1, -2, -2, 2, 2, -1, 1]
row_moves = [-2, -2, -1, 1, -1, 1, 2, 2]

# 시작 포인트에서 각 이동이 가능할 경우 count 증가 아니면 버리기
for i in range(len(column_moves)):
    # 열은 문자이므로 유니코드로 변환
    # 행은 문자이므로 숫자로 변환
    start_column = int(ord(point[:1]))-96
    start_row = int(point[1:])
    moved_column = chr(start_column + column_moves[i] + 96)
    moved_row = start_row + row_moves[i]
    if(moved_column >= 'a' and moved_column <= 'h' and moved_row >= 1 and moved_row <= 8):
        COUNT += 1
        
print(COUNT)


# 책의 답안에서는 나이트가 이동 가능한 8개의 방향을 하나의 배열에 저장하여 사용
# 나머지 로직은 비슷함.
# 체스판의 경계 주의 <- 실수했음.