import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())

energy_list = []
large_jump = False
dp = [INF for _ in range(n+1)]

for _ in range(n-1):
    temp = list(map(int, input().split()))
    energy_list.append(temp)

k = int(input())

A = [0] + [x[0] for x in energy_list]
B = [0] + [x[1] for x in energy_list]

# print(A)
# print(B)


# 구현부

# 돌이 하나면
if n == 1:
    print(0)


# 슈퍼점프를 사용하지 않고
dp[1] = 0
dp[2] = A[1] #1번에서 2번 돌로 갈 수 있는 경우는 S점프만 있기 때문


# S, M 점프 중 작은 것
for i in range(3, n+1):
    dp[i] = min(dp[i], dp[i-1] + A[i-1], dp[i-2]+B[i-2])
    print(f"i = {i}, dp = {dp}")

min_cost = dp[n]
print(dp[n])
print()

# L점프 넣었을 때

# n=5 -> 1 <= <3 => 1, 2
for i in range(1, n-2):
    # i에서 i+3으로 바로 점프
    super_jump = dp[i] + k

    if i+3 <= n:
        super_jump = min(super_jump, dp[i+3])
    if i+4 <= n:
        super_jump = min(super_jump, dp[i+4] + A[i+3])
    if i+5 <= n:
        super_jump = min(super_jump, dp[i+5] + B[i+3])
    
    min_cost = min(min_cost, super_jump)

    print(dp)