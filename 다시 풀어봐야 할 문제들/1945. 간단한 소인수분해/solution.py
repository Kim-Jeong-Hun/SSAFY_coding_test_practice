import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    # 결과 저장할 배열
    result = [0 for _ in range(5)]
    
    # 소수 저장할 배열
    prime_number = [2, 3, 5, 7, 11]
    
    for j in range(len(result)):
        while N % prime_number[j] == 0:
            N //= prime_number[j]
            result[j] += 1
    
    print(f"#{i}", end=' ')
    print(result[0], end=' ')
    print(result[1], end=' ')
    print(result[2], end=' ')
    print(result[3], end=' ')
    print(result[4])