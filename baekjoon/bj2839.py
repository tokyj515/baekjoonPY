
import sys

N = int(sys.stdin.readline())

dp = [9999] * 5001
dp[3] = 1
dp[5] = 1


for i in range(6, 5001):
	dp[i] = min(dp[i - 3], dp[i - 5]) + 1;



if dp[N] >= 9999:
	print("-1")

else:
	print(dp[N]);

