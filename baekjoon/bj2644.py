import sys


input = sys.stdin.readline




n = int(input())
p1, p2 = map(int, input().split())


graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]


# DFS
def dfs(graph, visited, v):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            depth[i] = depth[v] +1
            dfs(graph, visited, i)

    return -1


# 구현부
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(graph, visited, p1)


if depth[p2]:
    print(depth[p2])
else:
    print(-1)
