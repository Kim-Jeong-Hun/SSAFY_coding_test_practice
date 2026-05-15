# N X N 크기의 단어 퍼즐을 만들려고 한다.
# 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    # 세로 길이 N (가로의 길이이기도 함.), 단어의 길이 K
    N, K = map(int, input().split())

    # 2차원 배열 초기화
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 퍼즐의 각 셀이 1(문자가 들어갈 수 있는 칸), 0(문자가 들어갈 수 없는 칸)으로 나뉜다.
    # K 길이의 단어가 들어갈 수 있는 자리의 수를 출력해야 하므로

    # K 길이의 단어가 들어갈 수 있는 자리 카운트 변수
    count = 0

    # 행 체크
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    count += 1
                cnt = 0
        if cnt == K:
            count += 1

    # 열 체크
    for j in range(N):
        cnt = 0
        for i in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    count += 1
                cnt = 0
        if cnt == K:
            count += 1

    # 출력
    print(f"#{t} {count}")