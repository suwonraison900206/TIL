import sys
sys.stdin = open('5188.txt')

def backtracking(map_lst, point, a, b):
    global N
    global min_2
    if point > min_2: # 가지 치기, 최소보다 높은 값 들어오면 종료
        return
    if a == N-1 and b == N-1:  # 목표 좌표 도착시 최소값 비교 후 집어넣음
        if point < min_2:
            min_2 = point
            result.append(point)
        return
    if a + 1 < N:
        backtracking(map_lst, point + map_lst[a+1][b], a+1, b)
    if b + 1 < N:
        backtracking(map_lst, point + map_lst[a][b+1], a, b+1)

T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    lst = [list(map(int,input().split())) for __ in range(N)]
    start_point = lst[0][0]
    result = []
    min_2 = 10000000
    backtracking(lst, start_point, 0, 0)
    print('#{} {}'.format(test_case, min(result)))