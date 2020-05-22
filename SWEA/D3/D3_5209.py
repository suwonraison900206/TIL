import sys
sys.stdin = open('5209.txt')

def k (result, depth):
    global min_N
    if result > min_N:
        return
    if depth == N:
        if result < min_N:
            min_N = result
        return

    for j in range(N):
        if not visit_lst[j]:
            visit_lst[j] = 1
            k(result + lst[depth][j], depth + 1)
            visit_lst[j] = 0

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    lst= [list(map(int,input().split())) for __ in range(N)]
    min_N = 100000
    visit_lst = [0] * N

    for i in range(N):
        visit_lst[i] = 1
        k(lst[0][i], 1)
        visit_lst[i] = 0

    print('#{} {}'.format(test_case,min_N))