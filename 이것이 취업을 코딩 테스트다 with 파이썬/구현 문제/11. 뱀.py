import sys
sys.stdin = open("11. 뱀.txt")

N = int(input())
K = int(input())
apple_list = [list(map(int,input().split())) for __ in range(K)]
L = int(input())
snake_direction_list= [list(input().split()) for __ in range(L)]

map_list = [[0] * N for __ in range(N)]

for i in range(len(apple_list)):
    map_list[apple_list[i][0] -1][apple_list[i][1] -1] = 1

snake = (0,0)
stack = []

dir = [(0,1), (1,0), (0,-1), (-1,0)]
dir_num = 0
count = 0
stack.append(snake)

while True:
    k = stack.pop(-1)
    print(k)
    if len(snake_direction_list) != 0:
        if count == int(snake_direction_list[0][0]):
            if snake_direction_list[0][1] == 'D':
                dir_num = dir_num + 1
                snake_direction_list.pop(0)
                if dir_num == 4:
                    dir_num = 0
            elif snake_direction_list[0][1] == 'L':
                dir_num = dir_num - 1
                snake_direction_list.pop(0)
                if dir_num == -1:
                    dir_num = 3



    if (k[0] + dir[dir_num][0],k[1] + dir[dir_num][1]) in k:
        print(count)
        break


    if 0 <= k[0] + dir[dir_num][0] <= N-1 and 0 <= k[1] + dir[dir_num][1] <= N-1:

        if map_list[k[0] + dir[dir_num][0]][k[1] + dir[dir_num][1]] == 0:
            if len(stack) ==0:
                stack.append((k[0] + dir[dir_num][0], k[1] + dir[dir_num][1]))
            else:
                stack.pop(0)
                stack.append((k[0] + dir[dir_num][0], k[1] + dir[dir_num][1]))

        elif map_list[k[0] + dir[dir_num][0]][k[1] + dir[dir_num][1]] == 1:
            stack.append((k[0], k[1]))
            stack.append((k[0] + dir[dir_num][0], k[1] + dir[dir_num][1]))

        count = count + 1
    else:
        print(count +1)
        break





