# 백준 바이러스
from collections import deque

# 자료 입력
n = int(input())    # 컴퓨터의 개수
m = int(input())    # 쌍으로 연결된 수
computers = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    computers[x][y] = 1
    computers[y][x] = 1

visited = [False] * (n+1)
virus = []

# DFS
def dfs_virus(v):
    visited[v] = True
    virus.append(v)
    for i in range(1, n+1):
        if not visited[i] and computers[v][i] == 1:
            dfs_virus(i)


# BFS
def bfs_virus(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    virus.append(v)
    while queue:
        z = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and computers[z][i] == 1 :
                queue.append(i)
                visited[i] = True
                virus.append(i)


dfs_virus(1)
bfs_virus(1)

count_virus = len(virus) - 1
print(count_virus)
