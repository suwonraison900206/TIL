import copy


def solution(board):
    r_lst = []
    r_lst.append(([0,0],[0,1]))
    board_visit_list = copy.deepcopy(board)

    time = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    s_lst = []
    print(board)

    while r_lst:
        k = r_lst.pop()

        for i in range(4):
            count = 0
            for j in range(2):
                di = k[j][0] + dx[i]
                dj = k[j][1] + dy[i]

                if 0 <= di < len(board) and 0 <= dj < len(board) and board[di][dj] != 1:
                    count = count + 1
                    s_lst.append((di,dj))

            if count == 2:

                if board_visit_list[s_lst[0][0]][s_lst[0][1]] == 0 or board_visit_list[s_lst[1][0]][s_lst[1][1]] == 0:
                    time = time + 1
                    r_lst.append((s_lst, time))
                print(r_lst)
                print(r_lst[-1][-1])
                s_lst =[]









        if board_visit_list[k[0][0]][k[0][1]] == 0 or board_visit_list[k[1][0]][k[1][1]] == 0:
            board_visit_list[k[0][0]][k[0][1]] = 1
            board_visit_list[k[1][0]][k[1][1]] = 1
        break

    answer = 0
    return answer



board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
solution(board)