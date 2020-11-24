def solution(board, moves):
    result = []
    answer = 0


    while moves:

        k = moves.pop(0) - 1

        for i in range(len(board)):
            if board[i][k] != 0:
                result.append(board[i][k])
                board[i][k] = 0
                if len(result) > 1 and result[-1] == result[-2]:
                    result.pop()
                    result.pop()
                    answer +=2
                break
    print(answer)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)