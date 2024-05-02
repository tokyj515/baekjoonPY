import sys
sys.setrecursionlimit(10 ** 8)

N, M, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 연결 노트 역순 정렬
for i in range(N+1):
    graph[i].sort(reverse=True)


# dfs
cnt = 1

def dfs(graph, visited, v):
    global cnt

    visited[v] = 1
    answer[v] = cnt


    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph, visited, i)


dfs(graph, visited, start)

for i in answer[1:]:
    print(i)

