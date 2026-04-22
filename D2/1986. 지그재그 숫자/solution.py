import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def zigzag():
    # N 입력받기
    N = int(input())
    
    # 결과값 저장하기 위한 변수
    result = 0
    
    # 1부터 N까지 숫자를 더하기 위해 반복문
    for i in range(1, N+1):
        # 홀수면 더하기
        if i%2 == 1:
            result += i
        else:
            result -= i
            
    return result

for j in range(1, T+1):
    print(f"#{j} {zigzag()}")