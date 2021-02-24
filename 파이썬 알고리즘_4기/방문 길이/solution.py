def solution(dirs):
    answer = 0

    start = [0, 0]
    dirs = list(dirs)

    U = [-1, 0]
    D = [1, 0]
    R = [0, 1]
    L = [0, -1]
    check_list = []

    for dir in dirs:
        if dir == 'U':

            dx = start[0] + U[0]
            dy = start[1] + U[1]

            if -5 <= dx <= 5 and -5 <= dy <= 5:

                a = [start[0] + U[0], start[1] + U[1]]

                if [start + a] not in check_list:
                    check_list.append([start + a])
                    check_list.append([a + start])
                    answer += 1
                    start = a
                else:
                    start = a

        elif dir == 'D':

            dx = start[0] + D[0]
            dy = start[1] + D[1]

            if -5 <= dx <= 5 and -5 <= dy <= 5:

                a = [start[0] + D[0], start[1] + D[1]]

                if [start + a] not in check_list:
                    check_list.append([start + a])
                    check_list.append([a + start])

                    answer += 1
                    start = a
                else:
                    start = a

        elif dir == 'R':

            dx = start[0] + R[0]
            dy = start[1] + R[1]

            if -5 <= dx <= 5 and -5 <= dy <= 5:

                a = [start[0] + R[0], start[1] + R[1]]

                if [start + a] not in check_list:
                    check_list.append([start + a])
                    check_list.append([a + start])
                    answer += 1
                    start = a
                else:
                    start = a
        elif dir == 'L':

            dx = start[0] + L[0]
            dy = start[1] + L[1]

            if -5 <= dx <= 5 and -5 <= dy <= 5:

                a = [start[0] + L[0], start[1] + L[1]]
                if [start + a] not in check_list:
                    check_list.append([start + a])
                    check_list.append([a + start])
                    answer += 1
                    start = a
                else:
                    start = a

    return answer