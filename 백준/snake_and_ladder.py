import sys
sys.stdin = open('snake_and_ladder.txt')

N, M = map(int, input().split())
ladder_lst = [list(map(int, input().split())) for __ in range(N)]
snake_lst = [list(map(int, input().split())) for __ in range(M)]

lst = [0] * 100
visit = [0] * 100
count = 0
stack = [(1,0)]
stack2 = []


while stack:
    k = stack.pop(0)
    for i in range(1,7):
        for j in range(len(ladder_lst)):

            print(k[0] +i, ladder_lst[j][0])
            if k[0] + i == ladder_lst[j][0]:
                if visit[ladder_lst[j][0]] != 1:
                    visit[ladder_lst[j][0]] = 1
                    visit[ladder_lst[j][1]] = 1
                    stack2.append(((ladder_lst[j][1]), count+1))



            else:
                if visit[k[0] +i] != 1:
                    visit[k[0] + i] = 1
                    stack2.append((k[0] + i, count+1))

                    break

    if len(stack) == 0:
        print(stack2)

        stack = stack2[:]
        stack2 = []
        count = count + 1

        #
    #
    # for i in range(len(snake_lst)):
    #

