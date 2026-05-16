import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 결과 이득 변수
    result = 0

    # 구매한 물건의 총 가격
    total_buy = 0

    # 구매한 물건의 총 개수
    buy_cnt = 0

    # 날짜 카운트
    day_cnt = N

    # 가장 비싼날 가격
    highest = max(arr)

    # 배열 내부 날짜
    day = 0

    while day_cnt != 0:
        # 물건을 사는 날짜가 최고가보다 이전이고,
        # 최고가보다 작은 경우 구매
        if day < arr.index(highest) and arr[day] < highest:
            total_buy += arr[day]
            buy_cnt += 1
            day += 1
        # 최고가에 도달하면 판매하고 판매날까지의 데이터를 모두 제거 후 N일까지 반복
        # 물건이 1개 이상 있어야 판매 가능
        if day == arr.index(highest) and arr[day] == highest and buy_cnt >= 1:
            result += (highest * buy_cnt) - total_buy

            # 판매했으므로 이전 날들은 전부 배열에서 제거하고 갱신
            arr = arr[day+1:]
            if not arr:
                break

            # 구매한 물건 개수 카운트, 총 금액, 날짜 초기화
            buy_cnt = 0
            total_buy = 0
            day = 0
            # 최고가 새 배열의 최고가로 갱신
            highest = max(arr)
        # 하루가 지났으므로 날짜 변경
        day_cnt -= 1

    print(f"#{t} {result}")