def solution(m, n, board):

    def terminate(stack, board):

        for i in range(len(stack)):

            board[stack[i][0]][stack[i][1]] = 0
            board[stack[i][0] + 1][stack[i][1]] = 0
            board[stack[i][0]][stack[i][1] + 1] = 0
            board[stack[i][0] + 1][stack[i][1] + 1] = 0

        stack = []

        for i in range(len(board)-2, -1, -1):
            for j in range(len(board[i])):

                if board[i][j] !=0 and board[i+1][j] == 0:

                    act = 0
                    x = i
                    y = j
                    while act == 0:
                        board[x][y], board[x+1][y] = board[x+1][y] , board[x][y]

                        if x+1 < len(board)-1 and board[x+2][y] == 0:
                            x += 1
                        else:
                            act = 1

        for i in range(len(board) - 1):
            for j in range(n - 1):
                flag = board[i][j]
                if flag != 0 and board[i + 1][j] == flag and board[i][j + 1] == flag and board[i + 1][j + 1] == flag:
                    stack.append([i, j])
        if stack:
            terminate(stack, board)

    for i in range(len(board)):
        board[i] = list(board[i])

    stack = []
    for i in range(len(board)-1):
        for j in range(n-1):
            flag = board[i][j]
            if board[i+1][j] == flag and board[i][j+1] == flag and board[i+1][j+1] == flag:
                stack.append([i,j])

    if stack:
        terminate(stack , board)

    cnt = 0
    for i in range(len(board)):
        cnt = cnt + board[i].count(0)

    return cnt

m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
solution(m,n,board)