import sys

sys.stdin = open('공책구매.txt')

t = int(input())

for test_case in range(1, t+1):
    N, M = map(int,input().split())
    lst = [list(map(int,input().split())) for __ in range(M)]

    print(lst)
    lst.sort(key= lambda x: (x[1], x[2]))
    print(lst)


