from itertools import combinations ,permutations


def solution(orders, course):
    answer = []


    str_2 = ''

    for i in range(len(orders)):
        for j in range(len(orders[i])):
            if orders[i][j] not in str_2:
                str_2 = str_2 + orders[i][j]
    dict_all = {}

    for i in range(len(course)):
        k = list(combinations(str_2,course[i]))
        for j in range(len(k)):
            a = "".join(k[j])

            dict_all[a] = 0


    for i in range(len(orders)):
        for j in range(len(course)):
            try:

                q = list(combinations(orders[i], course[j]))
                print(q)
                for r in range(len(q)):
                    a = "".join(q[r])
                    if a in dict_all:
                        dict_all[a] += 1
                    pass
            except:
                pass


    print(dict_all)




    for key, value in dict_all.items():
        if value >= 2:
            answer.append([key, value])

    answer.sort(key=lambda x:x[1], reverse=True)
    print(answer)
    max_number = answer[0][1]
    cnt = answer[-1][1]
    while True:

        print(cnt)
        for i in range(len(answer)):
            if len(answer[i][0]) == len(answer[i+1][0]) and cnt > answer[i+1][1]:
                answer.pop(i+1)
                print(answer)
            elif len(answer[i][0]) != len(answer[i+1][0]):
                cnt = answer[i+1][1]
            break
        break



    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

solution(orders, course)