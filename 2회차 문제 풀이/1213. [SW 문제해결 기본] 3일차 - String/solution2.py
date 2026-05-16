import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")

T = 10

for _ in range(T):
    # 테스트 케이스 변수
    t = int(input())
    
    # 찾을 문자열 변수
    str_want_to_find = input()
    
    # 베이스 문자열 변수
    base_str = input()
    
    # 찾을 문자열 카운트 변수
    cnt = 0
    
    # 각 슬라이스해서 일일히 대조하는 방법
    target = len(str_want_to_find)
    for i in range(len(base_str)-target+1):
        if base_str[i:i+target] == str_want_to_find:
            cnt += 1

    print(f"#{t} {cnt}")