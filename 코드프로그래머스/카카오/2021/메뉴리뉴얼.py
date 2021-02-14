from itertools import permutations, combinations
def solution(orders, course):
    answer = []
    for i in course:
        dict = {}
        result = []
        for j in orders:

            for k in combinations(j, i):

                stack = ''.join(sorted(k))
                result.append(stack)

        for i in result:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1


        if dict:
            qwe = max(dict.values())

            if qwe == 1:
                pass
            else:

                for key, value in dict.items():
                    if value == qwe:
                        answer.append(key)


    answer.sort()
    print(answer)

    return answer
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders,course)

