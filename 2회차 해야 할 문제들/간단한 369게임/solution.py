# 숫자 1부터 차례대로 말하되, 3, 6, 9는 예외처리
# 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
# 박수는 횟수에 맞게 "-"를 출력한다.
# 완전 탐색 알고리즘

# 2자리 수 처리 방법
# 비교해서 3,6,9일 때마다 count 추가
# 출력은 한 번하여 해결

import sys
sys.stdin = open("input.txt", "r")

def game_369():
    N = int(input())
    
    clap = "-"
    
    for i in range(1, N+1):
        count = 0
        str_i = str(i)
        for j in str_i:
            if j == "3" or j == "6" or j == "9" :
                count += 1
        if (count > 0):
            print(count*clap, end=" ")
        else:
            print(i, end=" ")
    
game_369()