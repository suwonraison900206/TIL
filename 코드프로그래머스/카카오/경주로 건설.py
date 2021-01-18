def solution(board):
    def abc(x, y, north_flag, right_flag):

        for i in range(4):
            di = dx[i] + x
            dj = dy[i] + y

            if 0 <= di < len(board) and 0 <= dj < len(board) and board[di][dj] != 1:
                if i == 0 or i == 1:
                    if north_flag == 1:
                        if count_lst[di - dx[i]][dj - dy[i]] + 100 <= count_lst[di][dj]:
                            count_lst[di][dj] = count_lst[di - dx[i]][dj - dy[i]] + 100
                            abc(di, dj, 1, 0)
                    elif right_flag == 1:
                        if count_lst[di - dx[i]][dj - dy[i]] + 600 <= count_lst[di][dj]:
                            count_lst[di][dj] = count_lst[di - dx[i]][dj - dy[i]] + 600
                            abc(di, dj, 1, 0)


                elif i == 2 or i == 3:
                    if right_flag == 1:
                        if count_lst[di - dx[i]][dj - dy[i]] + 100 <= count_lst[di][dj]:
                            count_lst[di][dj] = count_lst[di - dx[i]][dj - dy[i]] + 100
                            abc(di, dj, 0, 1)
                    elif north_flag == 1:
                        if count_lst[di - dx[i]][dj - dy[i]] + 600 <= count_lst[di][dj]:
                            count_lst[di][dj] = count_lst[di - dx[i]][dj - dy[i]] + 600
                            abc(di, dj, 0, 1)

    count_lst = [[float('inf')] * len(board) for __ in range(len(board))]
    count_lst[0][0] = 0
    x = y = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):

        di = dx[i] + x
        dj = dy[i] + y

        if 0 <= di < len(board) and 0 <= dj <= len(board) and board[di][dj] != 1:
            if i == 0 or i == 1:
                count_lst[di][dj] = 100
                abc(di, dj, 1, 0)

            elif i == 2 or i == 3:
                count_lst[di][dj] = 100
                abc(di, dj, 0, 1)

    answer = count_lst[-1][-1]

    return answer


board = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
solution(board)