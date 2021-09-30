from collections import deque

N = int(input())
N_lst = [i+1 for i in range(N)]
N_lst = deque(N_lst)
if len(N_lst) == 1:
    print(1)
else:
    while True:

        q = N_lst.popleft()
        if len(N_lst) == 1:
            print(N_lst[0])
            break

        q1 = N_lst.popleft()
        N_lst.append(q1)



