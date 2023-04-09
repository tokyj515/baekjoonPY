import sys


def fibo(N):
    if N == 0 or N == 1:
        return dp[N]

    if dp[N] == 0:
        dp[N] = fibo(N - 2) + fibo(N - 1)

    return dp[N];


N = int(sys.stdin.readline())

dp = [0] * 95
dp[1] = 1

print(fibo(N))





