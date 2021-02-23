from collections import Counter
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
            print(result)

        dict = Counter(result)
        # for i in result:
        #     if i not in dict:
        #         dict[i] = 1
        #     else:
        #         dict[i] += 1
        print(dict)

        k = dict.most_common(2)
        print(k, 'kkkk')


    answer.sort()
    print(answer)

    return answer
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders,course)

