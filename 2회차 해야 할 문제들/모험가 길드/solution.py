# 문제점
# 현재 파티의 인원 변수를 만들지 않았음.
# -> 필요하다고 생각을 못했으며, 아직 조건을 세분화하는 과정이 부족하다고 느낌
# 변수 정의와 조건 문장 만드는 연습하기
# 조건 문장이 만들어지지 않으면 코드 한 줄도 쓰지 말기

import sys
sys.stdin = open("input.txt", "r")

N = int(input())

def party_making():
    player = list(map(int, input().split()))
    # 오름차순(공포도가 낮은 순서대로) 정렬
    player.sort()
    
    # 총 인원, 그룹
    total_player = len(player)
    group = 0
    
    # 현재 파티의 인원
    count = 0
    
    for fear in player:
        count += 1
        if count >= fear:
            group += 1
            count = 0        
    
    return group

print(party_making())