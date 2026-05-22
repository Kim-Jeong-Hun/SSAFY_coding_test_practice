import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for x in range(1, T+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    user_input = list(input())

    # 전차 위치 초기화
    spx, spy = 0, 0
    
    # 전차 바라보는 방향 초기화
    direction = ''
    
    # 전차의 현재 위치 찾는 함수
    def find_tank_position():
        global spx, spy, direction
        for i in range(H):
            for j in range(W):
                if matrix[i][j] == '^' or matrix[i][j] == 'v' or matrix[i][j] == '<' or matrix[i][j] == '>':
                    spx, spy = i, j
                    direction = matrix[i][j]

    for inp in user_input:
        # 일단 현재 전차 위치 찾기
        find_tank_position()

        # 명령이 U라면 한 칸 위가 맵 내의 위치인지 확인, 평지인지 확인
        # 조건을 만족하면 현재 있는 칸 평지로 표시하고, 건너간 칸으로 표시
        # 모든 방향에 표시
        if inp == 'U':
            if spx-1 >= 0 and spx-1 < H and spy >= 0 and spy < W and matrix[spx-1][spy] == '.':
                matrix[spx][spy] = '.'
                matrix[spx-1][spy] = '^'
            # 이동할 수 없는 상황이면 방향만 위로
            else:
                matrix[spx][spy] = '^'
        if inp == 'D':
            if spx+1 >= 0 and spx+1 < H and spy >= 0 and spy < W and matrix[spx+1][spy] == '.':
                matrix[spx][spy] = '.'
                matrix[spx+1][spy] = 'v'
            else:
                matrix[spx][spy] = 'v'
        if inp == 'L':
            if spx >= 0 and spx < H and spy-1 >= 0 and spy-1 < W and matrix[spx][spy-1] == '.':
                matrix[spx][spy] = '.'
                matrix[spx][spy-1] = '<'
            else:
                matrix[spx][spy] = '<'
        if inp == 'R':
            if spx >= 0 and spx < H and spy+1 >= 0 and spy+1 < W and matrix[spx][spy+1] == '.':
                matrix[spx][spy] = '.'
                matrix[spx][spy+1] = '>'
            else:
                matrix[spx][spy] = '>'

        # 현재 보는 방향으로 포탄 발사
        # 맵 밖으로 나가거나 벽에 충돌할때까지 직진
        # 벽돌벽이면 벽 파괴되어 평지됨. 강철벽이면 아무일 없음.
        if inp == 'S':
            # 방향이 위이면 0부터 현재 전차 위치-1의 행까지 칸을 모두 확인
            if direction == '^':
                for i in range(spx-1, -1, -1):
                    if matrix[i][spy] == '*':
                        matrix[i][spy] = '.'
                        break
                    elif matrix[i][spy] == '#':
                        break
            # 방향이 아래이면 현재 전차 위치+1부터 H-1까지 칸 확인
            if direction == 'v':
                for i in range(spx+1, H):
                    if matrix[i][spy] == '*':
                        matrix[i][spy] = '.'
                        break
                    elif matrix[i][spy] == '#':
                        break
            if direction == '<':
                for i in range(spy-1, -1, -1):
                    if matrix[spx][i] == '*':
                        matrix[spx][i] = '.'
                        break
                    elif matrix[spx][i] == '#':
                        break
            if direction == '>':
                for i in range(spy+1, W):
                    if matrix[spx][i] == '*':
                        matrix[spx][i] = '.'
                        break
                    elif matrix[spx][i] == '#':
                        break

    print(f"#{x}", end=' ')
    for i in range(H):
        print("".join(matrix[i]))