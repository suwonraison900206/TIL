# import sys
# sys.stdin = open("stone.txt")

T = int(input())

for test_case in range(T):
    N = int(input())
    lst = []
    lst2 =[]
    for i in range(N+2):
        lst.append([10000] * (N+2)) # 벽을 큰 값으로 씌였습니다
    for i in range(N):
        lst2.append(list(map(int,input().split())))


    for i in range(N):
        for j in range(N):
            lst[i+1][j+1] = lst2[i][j]

    visit_lst =[[0] * (N+2) for __ in range(N+2)] # 비지트 리스트도 벽 크기만큼 플러스 해서 만들었습니다.


    sum = 0 # 매장량
    sum_2 = 0 # 면적
    count = 0 # 숫자 판별
    stack = []
    # 모든방향 탐색
    dx =[-1, -1, -1, 0, 1, 1, 1, 0]
    dy =[-1, 0, 1, 1, 1, 0, -1, -1]
    max = 0
    min = 1000000000

    final_lst = [] # 매장량 저장
    final_lst2 = [] # 면적값 저장

    for i in range(1,N+1):
        for j in range(1, N+1):
            if lst[i][j] != 0 and lst[i][j] != 10000 and visit_lst[i][j] == 0: #0과 벽값을 제외하고 시작점을 찾습니다.
                visit_lst[i][j] = 1
                count = lst[i][j]
                sum = sum + count
                sum_2 = sum_2 + 1
                stack.append((i,j))
                while stack: # 스택 값이 없어질때 까지 탐색을 시작합니다
                    v = stack.pop()
                    for k in range(8): # dx dy 모든 방향 탐색
                        di = v[0] + dx[k]
                        dj = v[1] + dy[k]
                        if lst[di][dj] == count and visit_lst[di][dj] == 0: # 매장량 비교, 방문했는지 여부 비교
                            visit_lst[di][dj] = 1
                            sum = sum + count
                            sum_2 = sum_2 +1
                            stack.append((di,dj))

            if sum != 0: # 모든 매장량 더한 값과 면적크기를 각각 lst 와 lst2 에 넣습니다.
                final_lst.append(sum)
                final_lst2.append(sum_2)


            sum = 0
            sum_2 =0 # 다시 탐색 할때를 위해 초기화


    for i in range(len(final_lst)): # lst 값들을 비교해서 매장량 max 값을 찾아주고 max값이 같을때 min 값 비교해서 작은 값 출력
        if final_lst[i] > max:
            max = final_lst[i]
            min = final_lst2[i]
        elif final_lst[i] == max:
            if min > final_lst2[i]:
                min = final_lst2[i]

    print('#{} {} {}'.format(test_case + 1, max, min))
































