import sys
sys.stdin = open("스타트링크.txt")

import sys
sys.stdin = open("스타트링크.txt")

F, S, G, U, D = map(int, input().split())

visit_lst = [0] * (F+1)

stack = [S]
stack2 = []
visit_lst[S] = 1
select_lst = [U,-D]

cnt = 0
flag = 0

while stack:
    print(stack)
    q = stack.pop()

    if q == G:

        flag = 1
        break

    for i in select_lst:

        di = q + i

        if 0 < di < F+1 and visit_lst[di] == 0:

            visit_lst[di] = 1
            stack2.append(di)


    if not stack and stack2:

        stack = stack2[:]
        stack2 = []
        cnt +=1

if flag == 0:
    print("use the stairs")
else:

    print(cnt)