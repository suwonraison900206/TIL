def solution(n, computers):

    print(n, computers)

    visit_list = [0] * n

    print(visit_list, 'visit_lst')
    stack = []
    stack2 = []
    cnt = 0
    while visit_list.count(0) != 0:

        if not stack:
            cnt += 1
            for i in range(len(computers)):

                if visit_list[i] == 0:
                    for j in range(len(computers[i])):
                        if i == j:
                            continue
                        else:
                            if visit_list[j] == 0 and computers[i][j] == 1:
                                stack2.append(j)
                                visit_list[j] = 1
                print(stack2)
                stack = stack2[:]
                stack2 = []
                break

        else:
            for i in range(len(stack)):
                for j in range(len(computers[stack[i]])):

                    if i == j:
                        continue
                    else:
                        if visit_list[j] == 0 and computers[i][j] == 1:
                            stack2.append(j)
                            visit_list[j] = 1
            stack = stack2[:]
            stack2 = []

    print(cnt)

    answer = 0

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)