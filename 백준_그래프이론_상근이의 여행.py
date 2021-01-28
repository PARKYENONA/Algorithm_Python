# 백준 상근이의 여행
# 테스트 케이스 수 입력
t = int(input())

# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(t):
    n, m = map(int, input().split())
    parent = [0] * (n + 1)

    edges = []
    count = 0

    for i in range(1, n + 1):
        parent[i] = i

    # 모든 간선에 대한 정보를 입력받기
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    # 간선을 하나씩 확인
    for edge in edges:
        a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            count += 1
    print(count)
