import sys
sys.stdin = open("im.txt")

a = int(input())

for test_case in range(a):
    b = int(input())
    temp = []
    for i in range(b):
        temp.append(list(input()))

    print(temp)


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(b):
        for j in range(b):

            if temp[i][j] == 'A':

                for d in range(4):

                    di = i + dx[d]
                    dj = j + dy[d]
                    A_h = 1
                    k = 1
                    while 0 <= di < b and 0 <= dj < b and k <= A_h:

                        if temp[di][dj] == 'H':
                            temp[di][dj] = 'X'
                        di = di +dx[d]
                        dj = dj +dy[d]
                        k = k + 1

            elif temp[i][j] == 'B':

                for d in range(4):

                    di = i + dx[d]
                    dj = j + dy[d]
                    B_h = 2
                    k = 1
                    while 0 <= di < b and 0 <= dj < b and k <= B_h:

                        if temp[di][dj] == 'H':
                            temp[di][dj] = 'X'
                        di = di + dx[d]
                        dj = dj + dy[d]
                        k = k + 1

            elif temp[i][j] == 'C':

                for d in range(4):
                    di = i + dx[d]
                    dj = j + dy[d]
                    C_h = 3
                    k = 1
                    while 0 <= di < b and 0 <= dj < b and k <= C_h:

                        if temp[di][dj] == 'H':
                            temp[di][dj] = 'X'
                        di = di + dx[d]
                        dj = dj + dy[d]
                        k = k + 1

    print(temp)

    for i in range(b):
        for j in range(b):
            if temp[i][j] == 'H':
                cnt = cnt + 1

    print('#{} {}'.format(test_case + 1, cnt))