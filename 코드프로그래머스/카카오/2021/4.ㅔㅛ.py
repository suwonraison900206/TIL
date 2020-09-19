def bfs():
    pass


def solution(n, s, a, b, fares):
    visit_lst = [[0] * 2 for __ in range(n)]
    print(fares)
    stack = [(s, 0)]
    final_cnt_a = []
    final_cnt_b = []

    while stack:

        for j in range(len(stack)):
            q = stack.pop()
            for i in range(len(fares)):
                if fares[i][0] == q[0] or fares[i][1] == q[0]:
                    print(fares[i][0])

                    if fares[i][1] == a or fares[i][0] == a:
                        final_cnt_a.append(q[1] + fares[i][2])
                    elif fares[i][1] == b or fares[i][0] == b:
                        final_cnt_b.append(q[1] + fares[i][2])
                    else:
                        if fares[i][0] == q[0]:
                            stack.append((fares[i][1], q[1] + fares[i][2]))
                        elif fares[i][1] == q[0]:
                            stack.append((fares[i][0], q[1] + fares[i][2]))

        for i in range(len(fares)-1,-1,-1):
            if fares[i][0] == q[0] or fares[i][1] == q[0]:
                fares.pop(i)


        print(stack)
        print(final_cnt_a)
        print(final_cnt_b)
        print(fares)


    answer = 0
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)