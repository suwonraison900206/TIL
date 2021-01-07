def solution(board):
    max = 1
    print(board)

    k = len(board)
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            cnt = cnt + board[i][j]

    if cnt == 0:
        return 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):

            if board[i][j] == 0:
                continue
            board[i][j] = (min(board[i-1][j-1], board[i][j-1], board[i-1][j])) + 1

            if board[i][j] > max:
                max = board[i][j]
  

    return max * max

board = [[0,0,1,1],[1,1,1,1]]

solution(board)