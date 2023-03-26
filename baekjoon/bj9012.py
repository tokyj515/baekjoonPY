import sys

t = int(sys.stdin.readline())

for _ in range(t):
    st = []
    k = sys.stdin.readline()
    flag = True

    for e in k:
        if e == '(':
            st.append(e)
        elif e == ')':
           if st:
               st.pop()
           else:
               flag = False
               break


    if not st and flag: #스택이 비어있고, flag가 true
        print("YES")
    elif st or not flag:
        print("NO")

