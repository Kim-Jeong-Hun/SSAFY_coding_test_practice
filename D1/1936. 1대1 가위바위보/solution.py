import sys
sys.stdin = open("input.txt", "r")

# 가위는 1
# 바위는 2
# 보는 3
# 입력을 정수형으로 받으면 가위가 보를 이기는 경우를 제외하면 
# 숫자로 비교가 가능해서 편함
# 비기는 경우는 없음

a, b = map(int, input().split())

def rsp(num1, num2):
    winner = ''
    # A가 가위일 때
    if(num1 == 1):
        if(num2 == 2):
            winner = 'B'
        elif(num2 == 3):
            winner = 'A'
    # A가 바위일 때
    elif(num1 == 2):
        if(num2 == 1):
            winner = 'A'
        elif(num2 == 3):
            winner = 'B'
    # A가 보일 때
    else:
        if(num2 == 1):
            winner = 'B'
        elif(num2 == 2):
            winner = 'A'
    return print(winner)
    
rsp(a, b)