def solution(game_board, table):
    answer = -1
    pieces = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    cnt = 0
    visit_lst = [[0] * len(table) for __ in range(len(table))]
    board_check = [[0] * len(table) for __ in range(len(table))]
    board_visit_lst = [[0] * len(table) for __ in range(len(table))]


    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1 and visit_lst[i][j] == 0:
                piece_x = []
                piece_y = []
                piece_x.append(i)
                piece_y.append(j)
                stack.append([i,j])
                visit_lst[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for q in range(4):
                        di = x + dx[q]
                        dj = y + dy[q]
                        if -1 < di < len(table) and -1 < dj < len(table) and table[di][dj] == 1 and visit_lst[di][dj] == 0:
                            visit_lst[di][dj] = 1
                            piece_x.append(di)
                            piece_y.append(dj)
                            stack.append([di,dj])
                print(piece_x, piece_y)
                #
                # for bb in range(min_n, min_n +len(new_piece)):
                #     for nn in range(min_n, min_n +len(new_piece)):
                #         print(bb,nn)
                #         if table[bb][nn] == 1:
                #             if board_check[bb][nn] == 0:
                #                 board_check[bb][nn] = 1
                #                 new_piece[bb][nn] =1
                #
                # print(new_piece, 'b=new')
                # pieces.append(new_piece)

    print(pieces)
    while pieces:
        qqqqqqq = 0
        target = pieces.pop()
        flag_flags = 0
        for p in range(4):
            if flag_flags == 1:
                break
            target = [list(reversed(p)) for p in zip(*target)]
            real_cnt = 0
            false_cnt = 0
            for uuu in range(len(target)):
                for vvv in range(len(target)):
                    if target[uuu][vvv] == 1:
                        real_cnt +=1


            for xx in range(len(game_board) - len(target) + 1):
                for yy in range(len(game_board) - len(target) + 1):
                    stacks = []
                    flag = 0
                    for zz in range(len(target)):
                        for ww in range(len(target)):
                            if game_board[xx+zz][yy+ww] == 0 and target[zz][ww] == 1:
                                flag += 1
                                stacks.append([xx + zz, yy + ww])

                    if real_cnt == flag:
                        stacks2 = stacks[:]
                        count = 0
                        xxx = 0

                        for o, p in stacks:
                            count +=1

                            if board_visit_lst[o][p] == 1:
                               xxx = 1
                            else:
                                board_visit_lst[o][p] = 1
                        if xxx == 0:

                            cnt = cnt + count


                        while stacks:
                            kk = 0
                            board_x, board_y = stacks.pop()

                            for l in range(4):
                                board_di = board_x + dx[l]
                                board_dj = board_y + dy[l]
                                if -1 < board_di < len(game_board) and -1 < board_dj < len(game_board):
                                    if game_board[board_di][board_dj] == 0:
                                        if board_visit_lst[board_di][board_dj] == 0:
                                            kk = 1
                            if kk == 1:
                                break
                        print(cnt)
                #
                #         if kk == 1:
                #
                #             for oo, pp in stacks2:
                #
                #                 board_visit_lst[oo][pp] = 0
                #                 cnt -=1
                #         else:
                #             flag_flags = 1
                # if flag_flags == 1:
                #     break

    print(cnt)
    return cnt

#
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
solution(game_board, table)


# game_board = [[0,0,0,0,0,0,1,0,1,0,0,0],[1,1,1,1,1,1,0,0,0,1,0,0],[0,0,0,0,0,1,0,1,0,1,1,0],[1,0,1,1,1,0,1,0,1,0,0,1],[0,1,0,0,0,0,1,0,1,0,0,0],[0,0,1,1,1,0,1,0,1,1,0,1],[0,1,0,0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
# table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
# solution(game_board, table)

# game_board = [[0,0,1,0,0], [0,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[1,1,1,1,0]]
# table = [[1,1,0,1,1] , [1,0,0,1,1,],[0,0,0,1,1], [0,0,0,1,1], [0,0,0,0,1]]
# solution(game_board, table)

# game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
# table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
# solution(game_board, table)