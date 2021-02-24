from collections import Counter

def solution(board, nums):
    answer = 0
    nums = Counter(nums)

    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] in nums:
                board[i][j] = 0

    for i in board:  # 가로줄 빙고 체크
        if sum(i) == 0:
            answer += 1

    for i in zip(*board):  # 세로줄 빙고 체크
        if sum(i) == 0:
            answer += 1

    cnt = 0

    for i in range(len(board)):  # 대각선 체크
        cnt += board[i][i]
    if cnt == 0:
        answer += 1
    cnt = 0
    for i in range(len(board)):
        cnt = cnt + board[len(board) - 1 - i][i]

    if cnt == 0:
        answer += 1

    return answer