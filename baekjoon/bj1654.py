import sys

n, target_cnt = map(int, sys.stdin.readline().split(" "))
lines = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    lines.append(temp)

start = 1
end = max(lines)

while start <= end:
    mid = (start+end) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt >= target_cnt: # 너무 촘촘하니까 mid 뒤로 미루기
        start = mid + 1
    else:
        end = mid - 1


print(end)