from collections import deque

T = int(input())

for i in range(T):

    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst = deque(lst)

    for i in range(len(lst)):

        lst[i] = [i,lst[i]]

    count = 0
    if len(lst) == 1:
        print(1)
        continue
    while lst:

        q = lst.popleft()

        for j in lst:

            if j[1] > q[1]:

                lst.append(q)
                break
        else:
            count +=1
            if q[0] == M:
                print(count)

