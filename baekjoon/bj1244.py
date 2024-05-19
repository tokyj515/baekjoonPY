import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split(" ")))

switch.insert(0, 0)


tc = int(input())

for _ in range(tc):
    gender, v = map(int, input().split(" "))


    if gender == 1:
        for i in range(1, n+1):
            if i % v == 0:
                if switch[i] == 1:
                    switch[i] = 0
                else:
                    switch[i] = 1


    elif gender == 2:
        start = v - (v-1)
        end = v + (v-1)

        if start < 0:
            start = 1

        for i in range(start, v+1):
            if end+1-i <= n and switch[i] == switch[end+1-i]:
                if switch[i] == 1:
                    switch[i] = 0
                    switch[end+1-i] = 0
                else:
                    switch[i] = 1
                    switch[end+1-i] = 1




switch.pop(0)
for i in range(len(switch)):
    if i % 20 > 0:
        print(switch[i], end=" ")
    else:
        print()
        print(switch[i], end=" ")



