# 다시 풀어봐야 하는 문제

# (i, j)만 #
# 나머지는 +
# 어떻게 줄바꿈 문제를 해결하지?
# 각 줄마다 5번째 문자의 출력이 끝나면 print()로 줄넘김
# 5번째 문자까지 출력이 끝나지 않은 경우, end=""로 공백없이 이어나가기

for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end="")
        else: 
            print("+", end="")
    print()