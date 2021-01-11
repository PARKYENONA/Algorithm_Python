# 백준DFS BFS
from collections import deque

# 자료 입력
n, m ,v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n+1)

# DFS
def dfs(v):
    visited[v] = True
    print(v, end = " ")
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


#BFS
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = False
    print(v, end = " ")
    while queue:
        z = queue.popleft()
        for i in range(1, n+1):
            if visited[i] and graph[z][i] == 1:
                queue.append(i)
                visited[i] = False
                print(i, end = ' ')

dfs(v)
print()
bfs(v)
