import sys , copy
sys.stdin= open("청소년상어.txt", 'r', encoding='utf-8')

def shark_move(lst2, s):
    global result, final_result
    flag = 0
    stack = []
    for i in range(4):
        for j in range(4):
            if lst2[i][j][0] == 'shark':
                lst2[i][j][0] = 0
                flag = 1
                locate = lst2[i][j][1]
                dx = i + dir[locate][0]
                dy = j + dir[locate][1]

                while 0 <= dx < 4 and 0 <= dy < 4:
                    if lst2[dx][dy][0] != 0:
                        stack.append((dx, dy))
                    dx = dx + dir[locate][0]
                    dy = dy + dir[locate][1]
                lst2[i][j][1] = 10000
    if flag == 0 :
        stack.append((0, 0))

    if len(stack) != 0:
        for i in range(len(stack)):
            copy_map = copy.deepcopy(lst2)
            eating = copy_map[stack[i][0]][stack[i][1]][0]


            copy_map[stack[i][0]][stack[i][1]][0] = 'shark'
            fish_move(copy_map)
            shark_move(copy_map, s+eating)
    else:
        final_result.append(s)



def fish_move(lst):
    number = 1
    while number <= 16:
        flag = 0
        for i in range(4):
            if flag == 1:
                break
            for j in range(4):
                if flag == 1:
                    break
                if lst[i][j][0] == number:
                    locate_number = lst[i][j][1]
                    while flag == 0:
                        dx = i + dir[locate_number][0]
                        dy = j + dir[locate_number][1]
                        if 0 <= dx < 4 and 0 <= dy < 4 and lst[dx][dy][0] != 'shark' :
                            lst[i][j] , lst[dx][dy] = lst[dx][dy], lst[i][j]
                            lst[dx][dy][1] = locate_number
                            flag = 1
                            number = number + 1

                        else:
                            locate_number = (locate_number + 1) % 8
        if flag == 0:
            number = number + 1


a = [list(map(int,input().split())) for __ in range(4)]
final_result = []
fish_map = []
dir_map = []
final_result = []
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
result = 0
map_lst2 = []
for i in range(4):
    map_lst = []
    for j in range(4):
        map_lst.append([a[i][2*j], a[i][2*j+1] -1])
    map_lst2.append(map_lst)
shark_move(map_lst2, 0)

print(max(final_result))