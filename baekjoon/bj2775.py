T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    p = [[0 for col in range(n + 1)] for row in range(k + 1)]

    for i in range(1, n + 1):
        p[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for k in range(1, j + 1):
                p[i][j] += p[i - 1][k]
    print(p[i][j])