from itertools import permutations, combinations
def solution(orders, course):
    answer = []
    for i in range(len(course)):
        dict = {}
        for j in range(len(orders)):

            k = list(combinations(orders[j], course[i]))

            for q in range(len(k)):
                print(k[q])

                if k[q] not in dict:
                    dict[k[q]] = 1
                else:
                    dict[k[q]] += 1
        print(dict)
        if dict:
            if max(dict.values()) == 1:
                pass
            else:

                u =[k for k,v in dict.items() if max(dict.values()) == v]
        print(u, 'u')
        print(dict)

        answer.append(u)

    answer2 = []
    print(answer)
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            word =''
            for q in range(len(answer[i][j])):
                word = word + answer[i][j][q]

            if word not in answer2:
                answer2.append(word)

    answer3 = sorted(answer2)


    print(answer3)

    answer3.sort()
    print(answer3)




    return answer3

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders,course)

