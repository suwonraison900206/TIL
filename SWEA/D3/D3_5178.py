import sys
sys.stdin = open("5178.txt")


def backtrack(N):
    global lst
    global sum

    if N == 1:
        print(backtrack(2) + backtrack(3))
    else:
        q = N % 2
        w = N // 2
        while lst[N] == 0:
            if lst[2 ** (w+1) + q] != 0 and lst[2 ** (w+1) + (q+1)] != 0:
                lst[N] = lst[2 ** (w+1) + q] + lst[2 ** (w+1) + (q+1)]
                return lst[N]
            else:
                backtrack(2 ** (w+1) + q)
                backtrack(2 ** (w+1) + (q+1))
        else:
            return lst[N]

T = int(input())

for test_case in range(T):

    N, M, L = map(int,input().split())
    lst = []
    sum = 0
    for i in range(N+1):
        lst.append(0)

    for i in range(M):
        leaf_node = list(map(int,input().split()))
        lst[leaf_node[0]] = leaf_node[1]
    print('{} {}'.format(test_case+1, backtrack(L)))









