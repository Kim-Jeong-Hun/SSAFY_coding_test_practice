# 나는 단어의 각 요소를 대칭적으로 비교했지만
# 다른 사람은 그냥 단어 자체를 거꾸로 돌려서 원본과 같은지 확인하는 방법 사용
# 확실히 생각의 스펙트럼을 넓혀야겠다고 생각함.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    # 단어 입력
    word = input()
    
    # 결과 변수
    result = 0

    # 단어 길이의 반만큼만 반복문 수행하면 됨.
    # 대칭되는 부분이 같으면 1 저장
    # 아니면 0 저장
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            result = 1
        else:
            result = 0

    print(f"#{t} {result}")