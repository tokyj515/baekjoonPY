import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
maze = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    temp = list(input().rstrip())
    graph.append(temp)

queue = deque()
queue.append((0, 0))
maze[0][0] += 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny] == '1' and maze[nx][ny] == 0:
            queue.append((nx, ny))
            maze[nx][ny] = maze[x][y] + 1

print(maze[n - 1][m - 1])



# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# graph = []
# visited = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# for _ in range(n):
#     temp = list(map(int, list(input().rstrip())))
#     graph.append(temp)
#
#
# queue = deque()
#
# queue.append((0, 0))
# while queue:
#     x, y = queue.popleft()
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny] == 1:
#             graph[nx][ny] = graph[x][y] + 1
#             queue.append((nx, ny))
#
#
# # /
# print(graph[n-1][m-1])