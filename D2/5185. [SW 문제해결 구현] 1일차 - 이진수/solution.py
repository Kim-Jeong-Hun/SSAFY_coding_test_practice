import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):

    N, H = input().split()

    str1 = []

    for i in H:
        if i == 'A':
            str1.append('10')
        elif i == 'B':
            str1.append('11')
        elif i == 'C':
            str1.append('12')
        elif i == 'D':
            str1.append('13')
        elif i == 'E':
            str1.append('14')
        elif i == 'F':
            str1.append('15')
        else:
            str1.append(i)

    str2 = ''
    for i in range(len(str1)):
        d = int(str1[i])
        d = format(d, "04b")
        str2 += d

    print(f"#{t} {str2}")