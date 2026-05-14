# D1 급이라 손풀이용으로 넘기기

import sys
sys.stdin = open("input.txt", "r")

TC = int(input())

def simultaneous_equations():
    x, y = map(int, input().split())

    a = (x+y)//2
    b = x - a

    print(a, b)

for i in range(TC):
    simultaneous_equations()