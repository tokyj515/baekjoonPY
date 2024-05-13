import sys

n = sys.stdin.readline().rstrip()
op = sys.stdin.readline().rstrip()
m = sys.stdin.readline().rstrip()

answer = ''


# 한 자리 수
if len(n) == 1 and len(m) == 1:
    # 덧셈
    if op == '+':
        if n == '1' and m == '1':
            print('2')
        elif (n == '1' and m == '0') or (n == '0' and m == '1'):
            print('1')
        elif n == '0' and m == '0':
            print(0)
    # 곱셈
    elif op == '*':
        if n == '1' and m == '1':
            print('1')
        else:
            print('0')

# 한 자리수 이상
else:
    #덧셈
    if op == '+':
        length = max(len(n), len(m))

        # 자릿수 맞추기
        if len(n) < len(m):
            for _ in range(length - len(n)):
                n = '0' + n
        elif len(n) > len(m):
            for _ in range(length - len(m)):
                m = '0' + m

        # 덧셈 처리
        for a, b in zip(n, m):
            if a == '0' and b == '0':
                answer += "0"
            elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                answer += '1'
            elif a == '1' and b == '1':
                answer += '2'
    # 곱셈
    elif op == '*':
        for _ in range(len(m) - 1):
            n += "0"
        answer = n


    print(answer)