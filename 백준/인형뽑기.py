def solution(board, moves):
    answer = 0
    stack = []
    for i in range(len(moves)):
        if moves[i] != 0:
            for j in range(len(board)):
                if board[j][moves[i]-1] != 0:
                    stack.append(board[j][moves[i]-1])
                    board[j][moves[i]-1] = 0
                    break
    cnt = 1
    while cnt == 1:
        cnt = 0
        if len(stack) == 1 or len(stack) == 0:
            break
        else:
            for i in range(len(stack)-1):
                if stack[i] == stack[i + 1]:
                    answer += 2
                    stack.pop(i)
                    stack.pop(i)
                    cnt = cnt + 1
                    break
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board,moves)