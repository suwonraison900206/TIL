import sys
sys.stdin = open("5097.txt")

t = int(input())

for test_case in range(t):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))

    stack = []

    for i in range(M):
        stack.append(lst.pop(0))
        lst = lst + stack
        stack = []

    print('#{} {}'.format(test_case+1, lst[0]))

