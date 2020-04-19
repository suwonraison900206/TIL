import sys
sys.stdin = open("cube.txt")

t = int(input())

for test_case in range(t):

    turn = int(input())

    direction = list(input().split())

    print(turn)
    print(direction)

    cube =['w', 'y', 'r', 'o', 'g', 'b']
    cube_list = []
    f_c = []
    for i in range(len(cube)):
        cube_list = []
        for j in range(9):
            cube_list.append(cube[i])
        f_c.append(cube_list)
    print(f_c)
    for i in range(turn):
        if direction[i] == 'L-':
            f_c[0][6], f_c[2][0], f_c[1][0], f_c[3][2] = f_c[2][0], f_c[1][0], f_c[3][2], f_c[0][6]
            f_c[0][7], f_c[2][3], f_c[1][1], f_c[3][5] = f_c[2][3], f_c[1][3], f_c[3][5], f_c[0][7]
            f_c[0][8], f_c[2][6], f_c[1][2], f_c[3][8] = f_c[2][6], f_c[1][6], f_c[3][8], f_c[0][8]
        elif direction[i] == 'L+':
            f_c[0][6], f_c[2][0], f_c[1][0], f_c[3][2] = f_c[3][0], f_c[0][0], f_c[2][2], f_c[1][6]
            f_c[0][7], f_c[2][3], f_c[1][1], f_c[3][5] = f_c[3][3], f_c[0][3], f_c[2][5], f_c[1][7]
            f_c[0][8], f_c[2][6], f_c[1][2], f_c[3][8] = f_c[3][6], f_c[0][6], f_c[2][8], f_c[1][8]
        elif direction[i] == 'F-':
            f_c[0][0], f_c[4][0], f_c[1][0], f_c[5][2] = f_c[4][0], f_c[1][0], f_c[5][2], f_c[0][0]
            f_c[0][3], f_c[4][3], f_c[1][3], f_c[5][5] = f_c[4][3], f_c[1][3], f_c[5][5], f_c[0][3]
            f_c[0][6], f_c[4][6], f_c[1][6], f_c[5][8] = f_c[4][6], f_c[1][6], f_c[5][8], f_c[0][6]
        elif direction[i] == 'F+':
            f_c[0][0], f_c[4][0], f_c[1][0], f_c[5][2] = f_c[5][0], f_c[0][0], f_c[4][0], f_c[1][0]
            f_c[0][3], f_c[4][3], f_c[1][3], f_c[5][5] = f_c[5][3], f_c[0][3], f_c[4][3], f_c[1][3]
            f_c[0][6], f_c[4][6], f_c[1][6], f_c[5][8] = f_c[5][6], f_c[0][6], f_c[4][6], f_c[1][6]
        elif direction[i] == 'B-':
            f_c[0][0], f_c[3][0], f_c[1][6], f_c[2][2] = f_c[3][0], f_c[1][6], f_c[2][2], f_c[0][0]
            f_c[0][1], f_c[3][3], f_c[1][7], f_c[2][5] = f_c[3][3], f_c[1][7], f_c[2][5], f_c[0][1]
            f_c[0][2], f_c[3][6], f_c[1][8], f_c[2][8] = f_c[3][6], f_c[1][8], f_c[2][8], f_c[0][2]
        elif direction[i] == 'B+':
            f_c[0][0], f_c[2][2], f_c[1][6], f_c[3][0] = f_c[2][2], f_c[1][6], f_c[3][0], f_c[0][0]
            f_c[0][1], f_c[2][5], f_c[1][7], f_c[3][3] = f_c[2][5], f_c[1][7], f_c[3][3], f_c[0][1]
            f_c[0][2], f_c[2][8], f_c[1][8], f_c[3][6] = f_c[2][8], f_c[1][8], f_c[3][6], f_c[0][2]
        print(f_c)


    cnt = 0
    for i in range(1):
        for j in range(9):
            print(f_c[i][j], end='')
            cnt = cnt + 1
            if cnt == 3:
                print()
                cnt = 0

