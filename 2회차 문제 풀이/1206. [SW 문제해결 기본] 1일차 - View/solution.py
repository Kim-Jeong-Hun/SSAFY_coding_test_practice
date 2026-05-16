import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T+1):
    # 건물 개수 입력 (0 포함)
    N = int(input())

    # 1차원 배열로 처리하기로 했으므로 배열로 건물 층 수 저장
    buildings = list(map(int, input().split()))

    # 조망권이 확보된 세대 수 카운트 변수
    cnt = 0
    
    # 조망권 기준 거리
    standard = 2

    for i in range(standard, N-standard):
        # 처음에는 플래그 1
        flag = 1
        # 비교할 빌딩들 배열 생성
        # i-2부터 i+2까지 i를 제외한 빌딩이 있어야 하므로 range(i-2, i+2+1)
        compares = [buildings[x] for x in range(i-standard, i+standard+1) if x != i]
        for j in range(len(compares)):
            # 비교할 빌딩들보다 층수가 작으면 플래그 0으로 변경
            if buildings[i] <= compares[j]:
                flag = 0
        if flag == 1:
            cnt += buildings[i] - max(compares)

    print(f"#{t} {cnt}")