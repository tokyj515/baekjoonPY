import sys
from collections import deque


# def dfs(graph, r, c, visited):
#
#     # 범위 확인
#     if r <= 0 or r >= n+1 or c <= 0 or c >= m+1:
#         return false
#
#     # 현재 지점 유효
#     visited[r][c] = true
#
#     dfs()
#
#
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
#


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())

graph =[]
# visitd = [[] for _ in range(n)]

# 그래프 세팅
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(temp)


# print(graph)


# 최소 칸 -> BFS
def bfs():
    #큐 설정, 시작 위치 인덱스
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위 내인지
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 갈 수 있는 곳인지 아닌지
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    return graph[n-1][m-1]


print(bfs())

