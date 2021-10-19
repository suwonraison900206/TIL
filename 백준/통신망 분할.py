def dfs(x, y, N_lst2, check_lst):
    for q in range(len(N_lst2[y])):
        if N_lst2[y][q] == 1:
            if check_lst[x][q] == 0:
                check_lst[x][q] = 1
                dfs(x, q, N_lst2, check_lst)

N, M, Q = map(int,input().split())
wires = [list(map(int,input().split())) for __ in range(M)]
wire_dict = {}
for i, x in enumerate(wires):
    wire_dict[i] = x
cuts = [int(input()) for _ in range(Q)]
N_lst = [[0] * N for _ in range(N)]
result = []
for a, b in wires:
    N_lst[a - 1][b - 1] = 1
    N_lst[b - 1][a - 1] = 1

for cut in cuts:
    N_lst[wire_dict[cut-1][0]-1][wire_dict[cut-1][1]-1] = 0
    N_lst[wire_dict[cut - 1][1] - 1][wire_dict[cut - 1][0] - 1] = 0
    check_lst = [[0] * N for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if N_lst[i][j] == 1:
                if check_lst[i][j] == 0:
                    check_lst[i][j] = 1
                    dfs(i, j, N_lst, check_lst)  # 끊어진 간선 정보 토대로 dfs 진행

    print(check_lst)
    print(cut-1)
    print(check_lst[cut-1].count(1))





