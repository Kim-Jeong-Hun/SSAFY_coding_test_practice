# 기초적인 재귀/DFS 문제
# 단순히 N의 서브 노드만 구하는 문제로 착각
# 다시 풀어보기


import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def subtree():
    # 간선의 개수 E
    # 루트가 될 노드 N
    E, N = map(int, input().split())
    
    # 노드 번호는 1번부터 E+1번까지 존재하므로 리스트의 크기는 E+1
    # 문제에서는 이진 트리라고 명시하였으므로, 배열은 first_child, second_child 두 개가 필요
    first_child, second_child = [0 for _ in range(E+2)], [0 for _ in range(E+2)]
    
    # 부모-자식 입력 배열
    array = list(map(int, input().split()))
    
    # 입력된 배열이 부모-자식 관계이므로 2칸씩 건너가면서 순회
    for i in range(0, len(array), 2):
        # 부모의 첫번째 자식이 비어 있으면, 첫번째 자식 칸에 저장
        # 첫번째 자식 칸에 이미 노드가 들어있으면, 두번째 자식 칸에 저장
        if first_child[array[i]] == 0:
            first_child[array[i]] = array[i+1]
        else:
            second_child[array[i]] = array[i+1]
    
    # 노드를 각 배열에 저장 후, 재귀하며 카운트 시작
    def dfs(node):
        if node == 0:
            return 0
        # N을 루트로 하는 서브트리에는 N이 포함되므로 초기 개수는 1
        return 1 + dfs(first_child[node]) + dfs(second_child[node])
    
    return dfs(N)

for j in range(1, T+1):
    print(f"#{j} {subtree()}")