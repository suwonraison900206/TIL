import sys
sys.stdin = open("1258.txt")


t = int(input())
for test_case in range(t):
    row_c = int(input())
    visit = [[0] * row_c for _ in range(row_c)]
    entry_x, entry_y = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    case = []
    for i in range(row_c):
        case.append(list(map(int, input().split())))

    num = 0
    cnt = 0
    result = []
    for i in range(row_c):
        for j in range(row_c):
            if case[i][j] != 0 and visit[i][j] == 0:
                num = num + 1
                case[i][j] = num
                entry_x = i
                entry_y = j
                stack.append((entry_x, entry_y))
                result.append(cnt)
                cnt = 0

                while stack:
                    v = stack.pop()
                    if case[v[0]][v[1]] != 0:
                        for d in range(4):
                            di = v[0] + dx[d]
                            dj = v[1] + dy[d]

                            if 0 <= di < row_c and 0 <= dj < row_c:
                                if case[di][dj] != 0 and visit[di][dj] == 0:
                                    case[di][dj] = num
                                    visit[di][dj] = 1
                                    cnt = cnt + 1
                                    stack.append((di, dj))

    result.append(cnt)
    final_result = []

    for k in range(1, len(result)):
        index_list = []
        for i in range(row_c):
            for j in range(row_c):
                if case[i][j] == k:
                    index_list.append((i, j))

        final_result.append(index_list)

    for_list = []

    for i in range(len(final_result)):
        for_list.append(len(final_result[i]))

    for_list.sort()


    print('#{}'.format(test_case + 1), end=' ')
    print('{}'.format(num), end=' ')

    visit_list = [0] * len(for_list)


    array_list = []

    for i in range(len(for_list)):
        quest_list = []
        for j in range(len(final_result)):
            if for_list[i] == len(final_result[j]):

                quest_list.append(final_result[j][for_list[i] - 1][0] - final_result[j][0][0] + 1)
                quest_list.append(final_result[j][for_list[i] - 1][1] - final_result[j][0][1] + 1)

        array_list.append(quest_list)

    quee = 0
    for i in range(len(array_list)):
        if len(array_list[i]) == 2:
            print(array_list[i][0],end=' ')
            print(array_list[i][1], end=' ')
        elif len(array_list[i]) == 4 and quee == 0:
            if array_list[i][0] < array_list[i][2]:
                print(array_list[i][0],end=' ')
                print(array_list[i][1], end=' ')
                print(array_list[i][2], end=' ')
                print(array_list[i][3], end=' ')
                quee = quee + 1
            else:
                print(array_list[i][2], end=' ')
                print(array_list[i][3], end=' ')
                print(array_list[i][0], end=' ')
                print(array_list[i][1], end=' ')
                quee = quee + 1
    print()