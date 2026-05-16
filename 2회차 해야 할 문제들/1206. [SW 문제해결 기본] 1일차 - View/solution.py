import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    # print(buildings)

    # 조망권 확보 세대 수
    total = 0

    for i in range(2, N-2):
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            second = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
            total += buildings[i] - second
        else:
            continue

    print(f"#{t} {total}")