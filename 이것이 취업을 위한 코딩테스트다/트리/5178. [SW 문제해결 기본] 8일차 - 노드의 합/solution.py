import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def find():
    # 총 노드 개수, 리프 노드 개수, 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    
    # 노드 개수+1 만큼 만들기
    array = [0 for _ in range(N+1)]
    
    # 리프 노드 입력 받기
    for _ in range(M):
        index, value = map(int, input().split())
        array[index] = value
    
    # 부모 노드부터 역순으로 자식들의 합 계산
    for i in range(N//2, 0, -1):
        array[i] = array[2*i] + array[2*i+1]
    
    return array[L]  # L번째 노드의 값만 반환

for j in range(1, T+1):
    result = find()
    print(f"#{j} {result}")