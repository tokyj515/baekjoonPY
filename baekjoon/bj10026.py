import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# dfs
def dfs(gragh, visited, x, y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx and nx < n and 0 <= ny and ny < n) and not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
            dfs(gragh, visited, nx, ny)



# 구현부
visited = [[0 for _ in range(n)] for _ in range(n)]
graph = []
for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)


# 일반인
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(graph, visited, i, j)
            cnt += 1

print(cnt)



# 적록색맹
cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(graph, visited, i, j)
            cnt += 1

print(cnt)

