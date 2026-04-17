import sys
sys.stdin = open("input.txt", "r")

# N : 행의 개수
# M : 열의 개수

N, M = map(int, input().split(' '))

def num_card_game(N):
    minimum_but_maximum = 0
    for i in range(N):
        row = list(map(int, input().split(' ')))
        row.sort()
        if(row[0] > minimum_but_maximum):
            minimum_but_maximum = row[0]
    return minimum_but_maximum

print(num_card_game(N))