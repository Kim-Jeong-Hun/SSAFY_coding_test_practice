# 입력을 받는다
# 입력을 잘라서 월은 월 검증 로직, 일은 일 검증 로직을 돌려서
# 유효하면 문자열 형식으로 리턴
# 유효하지 않으면 -1로 리턴

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def calendar(n):    
    
    # 입력을 받아서 각각 year, month, day로 분리
    # int()로 변환 시 0이 없어지므로 그냥 문자열로 받기
    data = input()
    year, month, day = data[:4], data[4:6], data[6:]
    
    def valid():
        print(f"#{n} {year}/{month}/{day}")
        
    def invalid():
        print(f"#{n} -1")
    
    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        if(int(day) > 0 and int(day) < 32):
            valid()
        else:
            invalid()
    elif month in ["04", "06", "09", "11"]:
        if(int(day) > 0 and int(day) < 31):
            valid()
        else:
            invalid()
    elif month == "02":
        if(int(day) > 0 and int(day) < 29):
            valid()
        else:
            invalid()
    else:
        invalid()

for i in range(1, T+1):
    calendar(i)