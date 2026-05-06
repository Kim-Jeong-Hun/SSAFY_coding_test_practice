import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    # N은 소수점 아래가 12자리 이내인 실수
    N = float(input())
    divisor = 0.5
    answer = ''

    while N > 0:
        if N >= divisor:
            N -= divisor
            answer += '1'
        else:
            answer += '0'
        divisor /= 2


    if len(answer) > 12:
        print(f"#{t} overflow")
    else:
        print(f"#{t} {answer}")