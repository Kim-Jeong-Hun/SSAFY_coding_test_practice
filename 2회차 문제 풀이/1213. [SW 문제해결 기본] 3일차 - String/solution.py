import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")

T = 10

for _ in range(T):
    t = int(input())
    str_want_to_find = input()
    base_str = input()

    cnt = base_str.count(str_want_to_find)

    print(f"#{t} {cnt}")