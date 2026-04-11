import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def equal_inequal(n):
    mark = ""
    a, b = map(int, input().split())
    if(a > b): mark = ">"
    elif(a < b): mark = "<"
    else: mark = "="
    print(f"#{n} {mark}")


for i in range(1, T+1):
    equal_inequal(i)