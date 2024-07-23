import sys
from collections import Counter
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

write = input().rstrip()
correct = input().rstrip()
cnt = 0


def i_check(a, b):
    if (a == 'i') and (b in ['i', 'j', 'l']):
        return True
    return False

def v_check(a, b):
    if (a == 'v') and (b in ['v', 'w']):
        return True
    return False


write_cnt = Counter(write)
correct_cnt = Counter(correct)

write_cnt = sorted(write_cnt.items())
correct_cnt = sorted(correct_cnt.items())


print(write_cnt)
print(correct_cnt)




if len(write) != len(correct):
    for d1, d2 in zip(write_cnt, correct_cnt):
        print(d1, d2)

# 변환
else:
    for a, b in zip(write, correct):
            if a != b:
                if i_check(a, b): continue
                if v_check(a, b): continue
                cnt += 1


print(cnt)